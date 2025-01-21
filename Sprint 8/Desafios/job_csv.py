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

raw_df = spark.read.csv(source_file, header=True, inferSchema=True, sep="|")

filtered_raw_df = raw_df.filter(
    (raw_df["genero"] == "Drama,Romance") & (raw_df["anoLancamento"] == 2016)
)

ids_excluir = [
    "tt11656988", "tt13231658", "tt3526416", "tt4332342", "tt5181502", 
    "tt5253158", "tt5579684", "tt5804390", "tt5813104", "tt5904950", 
    "tt5933608", "tt6483040", "tt8344230", "tt8835590"
]

filtered_df = filtered_raw_df.filter(~col("id").isin(ids_excluir))

selected_columns = [
    "tituloPincipal", "tituloOriginal", "notaMedia", "numeroVotos",
    "personagem", "nomeArtista", "profissao", "anoNascimento",
    "anoFalecimento", "anoLancamento", "tempoMinutos"
]
cleaned_df = filtered_df.select(selected_columns)

data_atual = datetime.now().strftime("%Y/%m/%d")
cleaned_df.write.mode("overwrite").parquet(target_path + "/" + data_atual)

job.commit()
