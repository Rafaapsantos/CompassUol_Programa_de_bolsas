import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col
from awsglue.utils import getResolvedOptions


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializa o SparkContext e GlueContext para manipulação dos dados
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
# Inicializa o job do AWS Glue
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define os caminhos de entrada e saída
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Lê o arquivo CSV localizado no S3 como DynamicFrame
df_dynamic = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)

# Converte o DynamicFrame para DataFrame
df = df_dynamic.toDF()

# Filtra os dados para selecionar apenas as linhas do gênero "Drama,Romance" e do ano de lançamento 2016 que é o ano em que teve mais lançamentos de filmes de "Drama,Romance"
filtra_dados = df.filter(
    (col("genero") == "Drama,Romance") & (col("anoLancamento") == 2016)
)

# Lista de IDs IMDB de filmes que devem ser excluídos, pois não exixtem esses filmes na API do TMDB
ids_excluir = [
    "tt11656988", "tt13231658", "tt3526416", "tt4332342", "tt5181502", 
    "tt5253158", "tt5579684", "tt5804390", "tt5813104", "tt5904950", 
    "tt5933608", "tt6483040", "tt8344230", "tt8835590"
]

# Remove os filmes dos IDs que estão na lista acima
dados_filtrados = filtra_dados.filter(~col("id").isin(ids_excluir))

# Define as colunas que eu escolhi, para serem mantidas no DataFrame final
colunas_selecionadas = [
    "tituloPincipal", "tituloOriginal", "notaMedia", "numeroVotos",
    "personagem", "nomeArtista", "profissao", "anoNascimento",
    "anoFalecimento", "anoLancamento", "tempoMinutos", "id"
]
# Seleciona apenas as colunas relevantes
dados_limpos = dados_filtrados.select(*colunas_selecionadas)

dados_limpos.write.mode("overwrite").parquet(target_path)
 
job.commit()