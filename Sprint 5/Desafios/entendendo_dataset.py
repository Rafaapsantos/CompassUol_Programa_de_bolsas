import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('violencia_domestica_2023.csv', delimiter=';', encoding='utf-8')

# Exibir as primeiras linhas 
print(df.head())

# Checar as informações gerais do DataFrame
print(df.info())

