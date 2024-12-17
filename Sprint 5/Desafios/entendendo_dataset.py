import pandas as pd

# Carregar o arquivo C
df = pd.read_csv('violencia_domestica_2023.csv', delimiter=';', encoding='utf-8')

# Exibir as primeiras linhas para confirmar o carregamento
print(df.head())

# Checar as informações gerais do DataFrame
print(df.info())

# Verificar valores nulos
print("Valores nulos por coluna:\n", df.isnull().sum())

# Salvar o DataFrame tratado para uso no próximo script
df.to_csv('dados_tratados.csv', index=False, sep=';', encoding='utf-8')