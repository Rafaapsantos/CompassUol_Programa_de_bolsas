import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job  
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, size, when, row_number
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

# Remove as colunas que não serão mais utilizadas na análise
movies = movies.drop("budget", "titulopincipal", "personagem")

# Filtra os registros para remover as linhas que estiverem vazias na coluna 'production_countries'
movies = movies.filter(size(col("production_countries")) > 0)

# Filtra os registros para remover linhas que estiverem igual a '\N' na coluna 'anonascimento' (Vi isso quando fiz uma consulta no athena)
movies = movies.filter(col("anonascimento") != "\\N")

# Criação de tabelas dimensionais e fato, utilizando IDs sequenciais para cada dimensão

# Cria a dimensão 'dim_pais' com países únicos e gerando um ID sequencial
window_spec = Window.orderBy("origin_country")
dim_pais = movies.select("origin_country").distinct()
dim_pais = dim_pais.withColumn("id_pais", row_number().over(window_spec))

# Criando a dimensão 'dim_artista' com informações únicas de artistas
window_spec = Window.orderBy("nomeartista")
dim_artista = movies.select("nomeartista", "profissao", "anonascimento", "anofalecimento").distinct()
dim_artista = dim_artista.withColumn("id_artista", row_number().over(window_spec))

# Criando a dimensão 'dim_producao' com informações únicas de produção
window_spec = Window.orderBy("imdb_id")
dim_producao = movies.select("imdb_id", "titulooriginal", "original_language", "production_countries", "anolancamento").distinct()
dim_producao = dim_producao.withColumn("id_producao", row_number().over(window_spec))

# Criando a tabela fato 'fato_filme' com referências às dimensões criadas
fato_filme = movies\
    .join(dim_pais, "origin_country", "left")\
    .join(dim_artista, "nomeartista", "left")\
    .join(dim_producao, "imdb_id", "left")\
    .select("id_pais", "id_artista", "id_producao", "popularity", "notamedia", "numerovotos", "tempominutos")

# Adiciona uma chave primária sequencial para os filmes na tabela fato
window_spec = Window.orderBy("id_pais")
fato_filme = fato_filme.withColumn("id_filme", row_number().over(window_spec))

# Define o caminho de saída para os dados processados para a camada refined
output_path = "s3://datalake-rafaela-santos/refined/"

# Salva as tabelas dimensionais e a tabela fato no formato Parquet na camada refined do S3
dim_pais.write.mode("overwrite").parquet(f"{output_path}dim_pais/")
dim_artista.write.mode("overwrite").parquet(f"{output_path}dim_artista/")
dim_producao.write.mode("overwrite").parquet(f"{output_path}dim_producao/")
fato_filme.write.mode("overwrite").parquet(f"{output_path}fato_filme/")