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

# Captura a data atual para o caminho S3
data_atual = datetime.now().strftime('%Y/%m/%d')

# Caminhos locais e S3
nome_bucket = 'datalake-rafaela-santos'

arquivos_locais = {
    "movies.csv": "./dados/movies.csv",
    "series.csv": "./dados/series.csv"
}

caminhos_s3 = {
    "movies.csv": f"Raw/Local/CSV/Movies/{data_atual}/movies.csv",
    "series.csv": f"Raw/Local/CSV/Series/{data_atual}/series.csv"
}
# Faz o upload dos arquivos diretamente
for nome_arquivo, caminho in arquivos_locais.items():
    if os.path.isfile(caminho):  # Verifica se o arquivo existe
        try:
            s3_client.upload_file(caminho, nome_bucket, caminhos_s3[nome_arquivo])
            print(f" O arquivo {nome_arquivo} foi enviado com sucesso para {caminhos_s3[nome_arquivo]}")
        except Exception as e:
            print(f"Erro ao enviar {nome_arquivo}: {e}")
    else:
        print(f" O arquivo {nome_arquivo} não foi encontrado em {caminho}")
