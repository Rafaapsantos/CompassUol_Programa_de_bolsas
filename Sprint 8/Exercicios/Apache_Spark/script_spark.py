from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import rand, floor, when
from pyspark.sql import functions as F

# Iniciando uma SparkSession com um nome de aplicação
spark = SparkSession \
                .builder \
                .master("local[*]") \
                .appName("Exercicio Spark") \
                .getOrCreate()

## ETAPA 2
# Define o esquema para os dados do arquivo. Apenas uma coluna chamada Nomes
schema = StructType([StructField("Nomes", StringType(), True)])

# Lê os dados do arquivo 'nomes_aleatorios.txt' usando o esquema definido
df_nomes = spark.read.csv('./nomes_aleatorios.txt', schema=schema)
# Exibe o esquema do DataFrame para verificar se está correto
print("SCHEMA DO DATAFRAME")
df_nomes.printSchema()
# Mostra as primeiras 10 linhas do DataFrame
print("10 PRIMEIRAS LINHAS DO DATAFRAME")
df_nomes.show(10)

## ETAPA 3
# Lista de níveis de escolaridade
escolaridade = ["Fundamental", "Medio", "Superior"]
# Adiciona uma coluna 'Escolaridade' com valores aleatórios
df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, escolaridade[0]) # 33% de chance de ser "Fundamental"
    .when(rand() < 0.66, escolaridade[1]) # 33% de chance de ser "Medio"
    .otherwise(escolaridade[2]) # 34% de chance de ser "Superior"
)
df_nomes.show(10)

## ETAPA 4
# Lista de países da America do Sul
paises = ["Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"]
# Adiciona a coluna 'Pais' com valores aleatórios da lista de países
df_nomes = df_nomes.withColumn(
        "Pais",
        F.array(*[F.lit(pais) for pais in paises]).getItem(floor(rand() * len(paises)))
)
df_nomes.show(10)

## ETAPA 5
# Gera um ano aleatório entre 1945 e 2010
df_nomes = df_nomes.withColumn("AnoNascimento",
                               floor(rand() * (2010 - 1945 + 1)) + 1945)

## ETAPA 6
# Cria um novo DataFrame contendo apenas pessoas nascidas em 2000 ou depois
df_select = df_nomes.filter(df_nomes["AnoNascimento"] >= 2000).select("Nomes", "Escolaridade", "Pais", "AnoNascimento")
# Mostra até 100 registros filtrados
print("100 REGISTROS FILTRADOS")
df_select.show(100)

# ETAPA 7
#Cria uma visão temporária chamada "pessoas" para usar SQL diretamente no Spark
df_nomes.createOrReplaceTempView("pessoas")
# Executa uma consulta SQL para selecionar nomes e anos de nascimento a partir de 2000
spark.sql("""
SELECT nomes, AnoNascimento
FROM pessoas
WHERE AnoNascimento >= 2000
LIMIT 10
""")

## ETAPA 8
#Filtra os registros de pessoas nascidas entre 1980 e 1994
millenials = df_nomes.filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994)).select("Nomes")
# Conta quantos millennials existem
numero_millenials = millenials.count()
# Exibe o número de millennials
print(f'NÚMERO DE MILLENNIALS: {numero_millenials}')


## ETAPA 9
#Faz a mesma contagem de millennials, mas com uma consulta SQL
spark.sql("""
SELECT count(*)
FROM pessoas
WHERE AnoNascimento >= 1980 AND
      AnoNascimento <= 1994
""")

## ETAPA 10
#Agrupa os dados por "Pais" e gerações definidas por intervalos de anos de nascimento
df_geracao = spark.sql("""
            SELECT Pais, 
                CASE 
                    WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
                    WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
                    WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials (Geração Y)'
                    WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
                END AS Geracao,
                COUNT(*) AS Quantidade
            FROM pessoas
            GROUP BY Pais, Geracao
                    """)

# Ordena os resultados por país, geração e quantidade
df_geracao = df_geracao.orderBy("Pais", "Geracao", "Quantidade")
# Mostra os resultados agrupados
print("RESULTADOS AGRUPADOS")
df_geracao.show()