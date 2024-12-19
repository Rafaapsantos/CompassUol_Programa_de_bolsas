import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('violencia_domestica_2023.csv', delimiter=';', encoding='utf-8')

# Exibe as primeiras linhas 
print(df.head())

# Checa as informações gerais do DataFrame
print(df.info())

