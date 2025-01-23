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

# Lê o arquivo JSON localizado no S3 como DynamicFrame
df_dynamic = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="json",
)

# Converte o DynamicFrame para DataFrame
df = df_dynamic.toDF()

# Define as colunas que eu escolhi, para serem mantidas no DataFrame final
colunas_selecionadas = [
    "imdb_id", "budget", "production_countries",
    "popularity", "origin_country", "original_language"
]
# Seleciona apenas as colunas relevantes
dados_limpos = df.select(*colunas_selecionadas)

# Salva os dados no formato Parquet
dados_limpos.write.mode("overwrite").parquet(target_path)
 
job.commit()