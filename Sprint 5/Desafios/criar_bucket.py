import boto3

# Configura as credenciais da AWS
aws_access_key_id = 'aws_access_key_id'
aws_secret_access_key = 'aws_secret_access_key'
aws_session_token = 'aws_session_token'

# Cria um cliente S3 usando as minhas credenciais
s3_client = boto3.resource(
    's3',
    aws_access_key_id=aws_access_key_id, 
    aws_secret_access_key=aws_secret_access_key, 
    aws_session_token=aws_session_token
)

# Cria o Bucket
try:
    s3_client.create_bucket(
        Bucket='rafaela-santos-desafiosprint5', # Nomde do bucket
    )
    print(f"Bucket criado com sucesso") # Se o bucket for criado, printa essa mensagem
except Exception as e:
    print(f"Erro ao criar o bucket: {e}") # Se der algum erro ao criar o bucket, printa essa mensagem 
