import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
from pyspark.sql.functions import col


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

raw_df = spark.read.json(source_file)

selected_columns = [
    "imdb_id", "budget", "production_countries",
    "popularity", "origin_country", "original_language"
]
cleaned_df = raw_df.select(selected_columns)

data_atual = datetime.now().strftime("%Y/%m/%d")

cleaned_df.write.mode("overwrite").parquet(target_path + "/" + data_atual)

job.commit()
