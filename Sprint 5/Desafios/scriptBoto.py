import boto3
import os

access_key = os.environ.get('AWS_ACCESS_KEY_ID')
secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
region = os.environ.get('AWS_DEFAULT_REGION')
# 1. Configurações
BUCKET_NAME = 'nome-do-seu-bucket'  # Substitua pelo nome do seu bucket
FILE_PATH = 'violencia_domestica_2023.csv' # Substitua pelo caminho do seu arquivo
OBJECT_NAME = os.path.basename(FILE_PATH) # Extrai o nome do arquivo para usar no S3

# 2. Criar o cliente S3
s3_client = boto3.client('s3',
                    aws_access_key_id=access_key, 
                    aws_secret_access_key=secret_key, 
                    region_name=region)

try:
    # 3. Fazer o upload do arquivo
    s3_client.upload_file(FILE_PATH, BUCKET_NAME, OBJECT_NAME)
    print(f"Arquivo '{OBJECT_NAME}' carregado com sucesso para o bucket '{BUCKET_NAME}'.")
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")
