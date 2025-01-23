import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Parâmetros da Glue Job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos S3
input_path = "s3://datalake-rafaela-santos/Raw/TMDB/JSON/2025/01/17/"
output_path = "s3://datalake-rafaela-santos/Trusted/TMDB/Parquet/movies/2025/01/17/"

# Leitura do arquivo JSON
datasource = spark.read.json(input_path)

# Conversão para formato Parquet
datasource.write.mode("overwrite").parquet(output_path)

# Finalização do job
job.commit()