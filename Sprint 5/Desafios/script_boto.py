import boto3
import os

# Configura as credenciais da AWS
aws_access_key_id = 'aws_access_key_id'
aws_secret_access_key = 'aws_secret_access_key'
aws_session_token = 'aws_session_token'

nome_bucket = 'rafaela-santos-desafiosprint5'   # Varíavel com o nome do meu bucket, para ficar mais facil
nome_dataset = 'violencia_domestica_2023.csv'   # Varíavel com o nome do meu dataset
nome_object = os.path.basename(nome_dataset)    #  Varíavel que extrai o nome do dataset para usar no S3

# Cria um cliente S3 usando as minhas credenciais
s3_client = boto3.client(
   's3',
    aws_access_key_id=aws_access_key_id, 
    aws_secret_access_key=aws_secret_access_key, 
    aws_session_token=aws_session_token
)

# Faz o upload do dataset para dentro do bucket
try:
    s3_client.upload_file(nome_dataset, nome_bucket, nome_object) 
    print(f"O dataset {nome_object} foi carregado com sucesso para o bucket {nome_bucket}")
except Exception as e:
    print(f"Erro ao carregar o dataset: {e}")
