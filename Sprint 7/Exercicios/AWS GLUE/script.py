import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['S3_INPUT_PATH', 'S3_TARGET_PATH'])

source_file = args['S3_INPUT_PATH']  
target_path = args['S3_TARGET_PATH']  

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Leitura do arquivo CSV no S3
df = spark.read.option("header", "true").csv(source_file)

# Mostra o schema do dataframe
df.printSchema()

# Altera a caixa dos valores da coluna nome para maiúsculo
df_upper = df.withColumn("nome", F.upper(df["nome"]))

# Imprimi a contagem de linhas do dataframe
print(f"Contagem de linhas: {df_upper.count()}")

# Contagem de nomes agrupados pelas colunas ano e sexo, ordenados por ano de forma decrescente
contagem_agrupada = df_upper.groupBy("ano", "sexo").count().orderBy("ano", ascending=False)
contagem_agrupada.show()

# Nome feminino com mais registros e o ano 
nome_feminino_mais_registros = df_upper.filter(df_upper["sexo"] == "F") \
    .groupBy("nome", "ano").agg(F.sum("total").alias("total_registros")) \
    .orderBy(F.desc("total_registros")) \
    .limit(1)

nome_feminino_mais_registros.show()

# Nome masculino com mais registros e o ano 
nome_masculino_mais_registros = df_upper.filter(df_upper["sexo"] == "M") \
    .groupBy("nome", "ano").agg(F.sum("total").alias("total_registros")) \
    .orderBy(F.desc("total_registros")) \
    .limit(1)

nome_masculino_mais_registros.show()

# Conta o total de registros por ano, para as primeiras 10 linhas ordenadas pelo ano
contagem_por_ano = df_upper.groupBy("ano").agg(F.sum("total").alias("total_registros")) \
    .orderBy("ano", ascending=True).limit(10)

contagem_por_ano.show()

# Grava o conteúdo no S3 em formato JSON e particionado por sexo e ano
df_upper.write.mode("overwrite").partitionBy("sexo", "ano").json(target_path)