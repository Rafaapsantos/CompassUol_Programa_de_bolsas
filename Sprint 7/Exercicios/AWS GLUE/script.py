import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, count, upper, desc, max

## @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Leitura do arquivo CSV no S3
dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [args['S3_INPUT_PATH']]},
    format="csv",
    format_options={"withHeader": True, "separator": ","}
)

# Conversão para DataFrame
df = dynamic_frame.toDF()

# Imprime o schema
df.printSchema()

# Transformar os valores da coluna 'nome' para MAIÚSCULO
df = df.withColumn("nome", upper(col("nome")))

# Contagem de linhas no DataFrame
num_rows = df.count()
print(f"Total de linhas: {num_rows}")

# Agrupando por ano e sexo, contando nomes
grouped_df = df.groupBy("ano", "sexo").agg(count("*").alias("count_names")).orderBy(col("ano").desc())
grouped_df.show()

# Nome feminino mais frequente
female_df = df.filter(col("sexo") == "F").groupBy("nome").agg(count("*").alias("count"))
popular_female = female_df.orderBy(desc("count")).first()
if popular_female:
    female_name = popular_female["nome"]
    female_count = popular_female["count"]
    female_year = df.filter((col("nome") == female_name) & (col("sexo") == "F")) \
                    .groupBy("ano").agg(count("*").alias("count")) \
                    .orderBy(desc("count")).first()["ano"]
    print(f"O nome feminino mais popular foi '{female_name}' com {female_count} registros no ano {female_year}.")

# Nome masculino mais frequente
male_df = df.filter(col("sexo") == "M").groupBy("nome").agg(count("*").alias("count"))
popular_male = male_df.orderBy(desc("count")).first()
if popular_male:
    male_name = popular_male["nome"]
    male_count = popular_male["count"]
    male_year = df.filter((col("nome") == male_name) & (col("sexo") == "M")) \
                  .groupBy("ano").agg(count("*").alias("count")) \
                  .orderBy(desc("count")).first()["ano"]
    print(f"O nome masculino mais popular foi '{male_name}' com {male_count} registros no ano {male_year}.")

# Total de registros por ano (10 primeiros ordenados por ano crescente)
total_registros_por_ano = df.groupBy("ano").agg(count("*").alias("total_registros")).orderBy("ano").limit(10)
total_registros_por_ano.show()

# Gravação do DataFrame no S3 com particionamento por sexo e ano
target_path = args['S3_TARGET_PATH'] + "/frequencia_registro_nomes_eua"
df.write.partitionBy("sexo", "ano").mode("overwrite").json(target_path)

job.commit()
