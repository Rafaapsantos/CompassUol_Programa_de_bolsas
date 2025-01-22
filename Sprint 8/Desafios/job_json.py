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

# Lê o arquivo json localizado no S3
df = spark.read.json(source_file)

# Define as colunas que eu escolhi, para serem mantidas no DataFrame final
colunas_selecionadas = [
    "imdb_id", "budget", "production_countries",
    "popularity", "origin_country", "original_language"
]
# Seleciona apenas as colunas relevantes
dados_limpos = df.select(colunas_selecionadas)

# Pega a data atual no formato "YYYY/MM/DD" para ser usada como parte do caminho de saída no S3
data_atual = datetime.now().strftime("%Y/%m/%d")

# Escreve o DataFrame final no formato Parquet no caminho de saída, com particionamento baseado na data atual
dados_limpos.write.mode("overwrite").parquet(target_path + "/" + data_atual)

job.commit()