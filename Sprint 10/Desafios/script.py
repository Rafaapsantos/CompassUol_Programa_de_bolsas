import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, explode, row_number, size, when
from pyspark.sql.window import Window

# Inicializa o contexto do Glue
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Carrega os arquivos parquet da camada Trusted
movies_local = spark.read.parquet("s3://datalake-rafaela-santos/Trusted/Local/Parquet/movies/part-00000-09fee6ff-5973-44e6-98c7-80ea6bf2e701-c000.snappy.parquet")
movies_tmdb = spark.read.parquet("s3://datalake-rafaela-santos/Trusted/TMDB/Parquet/movies/2025/01/17/")

# Realiza a junção dos arquivos usando 'id' do csv e 'imdb_id' do TMDB
movies = movies_local.join(movies_tmdb, movies_local.id == movies_tmdb.imdb_id, "inner")

# Lista de imdb_id a serem removidos
ids_para_remover = [
    "tt3215826", "tt3344694", "tt3722726", "tt4996022", "tt5160154", "tt5509142", "tt5665940",
    "tt5883632", "tt6121564", "tt6229786", "tt6389310", "tt5011242", "tt5143826", "tt5211596",
    "tt5324962", "tt5468386", "tt5742306", "tt5843056", "tt5841956", "tt5819870", "tt5925180",
    "tt5974454", "tt6582868", "tt1740495", "tt2515180", "tt2547584", "tt2787570", "tt2707722",
    "tt3794028", "tt3777860", "tt4446472", "tt4613254", "tt4655294", "tt4746506", "tt4874298",
    "tt4921812", "tt4932154"
]

# Filtra os filmes para remover os imdb_id da lista
movies = movies.filter(~col("imdb_id").isin(ids_para_remover))

# Remove as colunas que não serão mais utilizadas na análise
movies = movies.drop("budget", "titulopincipal", "personagem")

# Filtra os registros para remover as linhas que estiverem vazias na coluna 'production_countries'
movies = movies.filter(size(col("production_countries")) > 0)

# Filtra os registros para remover linhas que estiverem igual a '\N' na coluna 'anonascimento'
movies = movies.filter(col("anonascimento") != "\\N")

# Converter para double
movies = movies.withColumn("notamedia", when(col("notamedia") == "\\N", None).otherwise(col("notamedia").cast("double")))

# Converter para int
colunas_int = ["numerovotos", "anofalecimento", "anonascimento", "anolancamento", "tempominutos"]
for nome_colunas in colunas_int:
    movies = movies.withColumn(nome_colunas, when(col(nome_colunas) == "\\N", None).otherwise(col(nome_colunas).cast("int")))

# Tratamento de origin_country
movies = movies.withColumn("origin_country", explode(col("origin_country")))

# Tratamento de production_countries
movies = movies.withColumn("production_countries", explode(col("production_countries")))
movies = movies.withColumn("production_countries", col("production_countries.iso_3166_1"))

# Criação de tabelas dimensionais e fato, utilizando IDs sequenciais para cada dimensão

# Cria a dimensão 'dim_pais' com países únicos e gerando um ID sequencial
window_spec = Window.orderBy("origin_country")
dim_pais = movies.select("origin_country").distinct()
dim_pais = dim_pais.withColumn("id_pais", row_number().over(window_spec))

# Cria a dimensão 'dim_producao' com informações únicas de produção
window_spec = Window.orderBy("imdb_id")
dim_producao = movies.select("imdb_id", "titulooriginal", "original_language", "anolancamento").distinct()
dim_producao = dim_producao.withColumn("id_producao", row_number().over(window_spec))

# Criando a dimensão 'dim_artista' com informações únicas de artistas
window_spec = Window.orderBy("nomeartista")
dim_artista = movies.select("nomeartista", "profissao", "anonascimento", "anofalecimento").distinct()
dim_artista = dim_artista.withColumn("id_artista", row_number().over(window_spec))

# Criando a dimensão 'dim_pais_producao' com informações únicas do país da produção
window_spec = Window.orderBy("production_countries")
dim_pais_producao = movies.select("production_countries").distinct()
dim_pais_producao = dim_pais_producao.withColumn("id_pais_producao", row_number().over(window_spec))

# Criando a tabela fato 'fato_filme' com referências às dimensões criadas
fato_filme = movies\
    .join(dim_pais, "origin_country", "left")\
    .join(dim_artista, "nomeartista", "left")\
    .join(dim_producao, "imdb_id", "left")\
    .join(dim_pais_producao, "production_countries", "left")\
    .select("id_pais", "id_artista", "id_producao","id_pais_producao", "popularity", "notamedia", "numerovotos", "tempominutos")

# Adiciona uma chave primária sequencial para os filmes na tabela fato
window_spec = Window.orderBy("id_pais")
fato_filme = fato_filme.withColumn("id_filme", row_number().over(window_spec))

# Define o caminho de saída para os dados processados para a camada refined
output_path = "s3://datalake-rafaela-santos/Refined/"

# Salva as tabelas dimensionais e a tabela fato no formato Parquet na camada refined do S3
dim_pais.write.mode("overwrite").parquet(f"{output_path}dim_pais/")
dim_artista.write.mode("overwrite").parquet(f"{output_path}dim_artista/")
dim_producao.write.mode("overwrite").parquet(f"{output_path}dim_producao/")
dim_pais_producao.write.mode("overwrite").parquet(f"{output_path}dim_pais_producao/")
fato_filme.write.mode("overwrite").parquet(f"{output_path}fato_filme/")

# Finaliza o job do Glue
job.commit()