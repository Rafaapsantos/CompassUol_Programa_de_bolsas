import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Inicializa o contexto do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos S3
input_path = "s3://datalake-rafaela-santos/Raw/TMDB/JSON/2025/01/17/"
output_path = "s3://datalake-rafaela-santos/Trusted/TMDB/Parquet/movies/2025/01/17/"

# Lê os arquivos JSON
datasource = spark.read.json(input_path)

# Salva os dados em formato Parquet no destino especificado
datasource.write.mode("overwrite").parquet(output_path)

# Finaliza o job
job.commit()