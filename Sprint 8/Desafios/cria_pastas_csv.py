import boto3

# Configura as credenciais da AWS
aws_access_key_id = 'aws_access_key_id'
aws_secret_access_key = 'aws_secret_access_key'
aws_session_token = 'aws_session_token'

# Cria um cliente S3 usando as credenciais
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

# Nome do bucket
bucket_name = "datalake-rafaela-santos"

# Caminho das pastas que quero criar
folder_path = "Trusted/Local/Parquet/movies/"

# Função que cria a estrutura de pastas no S3
def create_s3_folder(s3_client, bucket_name, folder_path):
    # Cria a pasta enviando um objeto com uma barra no final do nome
    s3_client.put_object(Bucket=bucket_name, Key=(folder_path if folder_path.endswith("/") else folder_path + "/"))
    print(f"A pasta '{folder_path}' foi criada com sucesso no bucket '{bucket_name}'.")

# Chama a função
create_s3_folder(s3_client, bucket_name, folder_path)
