import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
from pyspark.sql.functions import col


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializa o SparkContext e GlueContext para manipulação dos dados
sc = SparkContext()
glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
# Inicializa o job do AWS Glue
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define os caminhos de entrada e saída
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Lê o arquivo CSV localizado no S3
df = spark.read.csv(source_file, header=True, inferSchema=True, sep="|")

# Filtra os dados para selecionar apenas as linhas do gênero "Drama,Romance" e do ano de lançamento 2016 que é o ano em que teve mais lançamentos de filmes de "Drama,Romance"
filtra_dados = df.filter(
    (df["genero"] == "Drama,Romance") & (df["anoLancamento"] == 2016)
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
    "anoFalecimento", "anoLancamento", "tempoMinutos"
]
# Seleciona apenas as colunas relevantes
dados_limpos = dados_filtrados.select(colunas_selecionadas)

# Pega a data atual no formato "YYYY/MM/DD" para ser usada como parte do caminho de saída no S3
data_atual = datetime.now().strftime("%Y/%m/%d")

# Escreve o DataFrame final no formato Parquet no caminho de saída, com particionamento baseado na data atual
dados_limpos.write.mode("overwrite").parquet(target_path + "/" + data_atual)

job.commit()