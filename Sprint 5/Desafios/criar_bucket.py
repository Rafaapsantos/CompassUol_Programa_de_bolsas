import boto3
import os

# A maneira correta de obter as credenciais do ambiente (se configuradas corretamente)
access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = os.getenv('AWS_DEFAULT_REGION')

# Verifique se as credenciais e região estão definidas
if not access_key or not secret_key or not region:
    print("Certifique-se de que as variáveis de ambiente estão configuradas corretamente.")
    exit()

# Configuração do cliente S3 com a região definida diretamente
s3_client = boto3.client('s3',
                         aws_access_key_id=access_key, 
                         aws_secret_access_key=secret_key, 
                         region_name=region)

# Nome do bucket e região
bucket_name = 'RAFAELA-DESAFIOSPRINT5'

# Criar o bucket
try:
    s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region}
    )
    print(f"Bucket '{bucket_name}' criado com sucesso na região {region}.")
except Exception as e:
    print(f"Erro ao criar o bucket: {e}")
