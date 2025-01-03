import boto3
import os
from datetime import datetime

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

# Pega a data atual no formato YYYY/MM/DD para criar os caminhos no bucket S3
data_atual = datetime.now().strftime('%Y/%m/%d')

# Nome do bucket onde os arquivos serão armazenados
nome_bucket = 'datalake-rafaela-santos'

# Define os caminhos locais para os arquivos que vão ser enviados
arquivos_locais = {
    "movies.csv": "./dados/movies.csv", # Caminho do arquivo movies.csv no diretório local
    "series.csv": "./dados/series.csv" # Caminho do arquivo series.csv no diretório local
}

# Define os caminhos de destino no bucket 
caminhos_s3 = {
    "movies.csv": f"Raw/Local/CSV/Movies/{data_atual}/movies.csv", # Caminho para movies.csv no bucket
    "series.csv": f"Raw/Local/CSV/Series/{data_atual}/series.csv" # Caminho para series.csv no bucket 
}

# Itera sobre os arquivos definidos nos caminhos locais
for nome_arquivo, caminho in arquivos_locais.items():
    if os.path.isfile(caminho):  # Verifica se o arquivo existe
        try:
            # Faz o upload do arquivo para o bucket
            s3_client.upload_file(caminho, nome_bucket, caminhos_s3[nome_arquivo])
            print(f" O arquivo {nome_arquivo} foi enviado com sucesso para {caminhos_s3[nome_arquivo]}")
        except Exception as e:
            # Exibe erros que possam ocorrer durante o upload
            print(f"Erro ao enviar {nome_arquivo}: {e}")
    else:
        # Exibe uma mensagem caso o arquivo não seja encontrado no caminho local
        print(f" O arquivo {nome_arquivo} não foi encontrado em {caminho}")
