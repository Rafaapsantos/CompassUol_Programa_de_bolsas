import boto3
import pandas as pd
import os

# Configura as credenciais da AWS
aws_access_key_id = 'aws_access_key_id'
aws_secret_access_key = 'aws_secret_access_key'
aws_session_token = 'aws_session_token'

nome_bucket = 'rafaela-santos-desafiosprint5'   # Varíavel com o nome do meu bucket, para ficar mais facil
nome_dataset_s3 = os.path.basename('violencia_domestica_2023.csv')  # Varíavel com o nome do objeto no S3
nome_dataset_transformado = 'dados_transformados.csv' # Varíavel com o nome do arquivo que foi transformado no S3


# Cria um cliente S3 usando as minhas credenciais
s3_client = boto3.client(
   's3',
    aws_access_key_id=aws_access_key_id, 
    aws_secret_access_key=aws_secret_access_key, 
    aws_session_token=aws_session_token
)

try:
    # Lê o dataset que eu coloquei no S3
    objeto = s3_client.get_object(Bucket=nome_bucket, Key=nome_dataset_s3)
    df = pd.read_csv(objeto['Body'], delimiter=';', encoding='utf-8')

    # 4.1- Cláusula que filtra dados usando ao menos dois operadores lógicos
    # Filtra apenas os dados de "Interior de MG" e "CONSUMADO"
    filtered_df = df[
        (df['rmbh'] == '3) Interior de MG') & 
        (df['tentado_consumado'] == 'CONSUMADO')
    ].copy()

    # 4.2- Duas funções de agregação
    # Função de agregação 1: Soma do número total de vítimas por município
    soma_vitimas = filtered_df.groupby('municipio_fato')['qtde_vitimas'].sum()

    # Função de agregação 2: Faz a média do número de vítimas por município
    media_vitimas = filtered_df.groupby('municipio_fato')['qtde_vitimas'].mean()

    # Obtem os 5 municípios com as maiores médias de vítimas
    top_5_municipios = media_vitimas.sort_values(ascending=False).head(5)

    # 4.3- Função condicional
    # Cria uma nova coluna indicando se o número de vítimas foi maior ou igual a 5 é considerdo Grave, senão
    # é considerado Leve
    filtered_df['vitimas_grave'] = filtered_df['qtde_vitimas'].apply(lambda x: 'Grave' if x >= 5 else 'Leve')

    # 4.4- Função de conversão
    # Converte a coluna "data_fato" para datetime
    filtered_df['data_fato'] = pd.to_datetime(filtered_df['data_fato'], dayfirst=True)

    # 4.5- Função de data
    # Cria uma nova coluna indicando True se o fato ocorreu no sábado ou no domingo e False se o fato ocorreu de segunda á sexta
    filtered_df['fim_de_semana'] = filtered_df['data_fato'].dt.weekday.isin([5, 6])

    # 4.6- Função de string
    # Transforma o nome do município para a primeira letra maiúscula e o resto das letras minúsculas
    filtered_df['municipio_fato'] = filtered_df['municipio_fato'].str.capitalize()

    # Printa as 5 maiores médias
    print(f"As 5 maiores quantidades médias de vítimas por município no interior de MG (2023, delitos consumados):\n {top_5_municipios} ")

    # Salva o DataFrame localmente
    filtered_df.to_csv(nome_dataset_transformado, index=False, sep=';', encoding='utf-8')

    # Carrega o arquivo local para o S3
    s3_client.upload_file(nome_dataset_transformado, nome_bucket, nome_dataset_transformado)
    print(f"O arquivo transformado com o nome -> {nome_dataset_transformado} foi salvo no bucket {nome_bucket}")

except Exception as e:
    print(f"Erro ao processar o arquivo: {e}")