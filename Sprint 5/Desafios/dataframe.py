import pandas as pd

# Carregar os dados tratados
df = pd.read_csv('violencia_domestica_2023.csv', delimiter=';', encoding='utf-8')

# 3.1. Cláusula que filtra dados usando ao menos dois operadores lógicos
# Filtrar apenas os dados de "Interior de MG" e "CONSUMADO"
filtered_df = df[
    (df['rmbh'] == '3) Interior de MG') & 
    (df['tentado_consumado'] == 'CONSUMADO')
].copy()

# 3.2. Duas funções de agregação
# Função de agregação 1: Soma do número total de vítimas por município
soma_vitimas = filtered_df.groupby('municipio_fato')['qtde_vitimas'].sum()

# Função de agregação 2: Média do número de vítimas por município
media_vitimas = filtered_df.groupby('municipio_fato')['qtde_vitimas'].mean()

# Obter os 5 municípios com as maiores médias de vítimas
top_5_municipios = media_vitimas.sort_values(ascending=False).head(5)

# 3.3. Função condicional
# Criar uma nova coluna indicando se o número de vítimas foi maior ou igual a 5
filtered_df['vitimas_grave'] = filtered_df['qtde_vitimas'].apply(lambda x: 'Grave' if x >= 5 else 'Leve')

# 3.4. Função de conversão
# Converter a coluna "data_fato" para datetime
filtered_df['data_fato'] = filtered_df['data_fato'].astype('datetime64[ns]')

# 3.5. Função de data
#Crie uma nova coluna indicando se o fato ocorreu em um sábado ou domingo:
filtered_df['fim_de_semana'] = filtered_df['data_fato'].dt.weekday.isin([5, 6])

# 3.6. Função de string
# Transformar o nome do município para a primeira letra maiúscula e o resto das letras minúsculas
filtered_df['municipio_fato'] = filtered_df['municipio_fato'].str.capitalize()

# Salvar o DataFrame final com as transformações
filtered_df.to_csv('dados_transformados.csv', index=False, sep=';', encoding='utf-8')

# Resultado final - Respondendo a pergunta
print("As 5 maiores quantidades médias de vítimas por município no interior de MG (2023, delitos consumados):")
print(top_5_municipios)
