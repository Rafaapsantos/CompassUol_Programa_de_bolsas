import boto3
import os
from datetime import datetime

# Configura as credenciais da AWS
aws_access_key_id = 'ASIAWQUOZ35IWKL7QF37'
aws_secret_access_key = 'NWekgL+Vk95S8XQMRgnxZlVnGZRSRc9aI/i8YOSN'
aws_session_token = 'IQoJb3JpZ2luX2VjEAIaCXVzLWVhc3QtMSJIMEYCIQDJOruMIuOHFtcU69Sam4gecSFj6e0f+4ZrJKLgmQQfHgIhAN1ERdDEkEA8p4FAII1qpA67sqhC6nVovDVypl7NK0vdKqoDCNv//////////wEQABoMNDQ4MDQ5ODMxNzYxIgxqiRm5Vwg398okZ6Aq/gIiSFHk6TAI7+ysLzlUQ4Z0G62dcD/dYLZimDV/AXfiSKYOHd2ePfLEEgcd0sqVQA0WuenbgzsFAD+cBPX4ivKf5fTHq7tNokbWPFsE84xrL5RJsaCho4qu93b+PXheNjvJw79zb+GVViOduaVQfcqG7fsE/lo2U9jPIMGoP8TnYp88qEZ9/Tb+UWFns/81Rupoy6X7Bd3jPMUA5krZnYERyDxFpZS4QnAyq/MCUj2fN21R/IAURSErYtnQxchifRYAf8ZbOQk5WtNHOb8b+OteGXLskuOvtx5UFsB/qpbJNxl6Hg0T7tZTnY6S4lXRtY2W8TnZnqd/ppn/mRUgD3t2ChLroQ10Bb5ExMEzinI1soIQEotf2Ct0Os2u1iZYvc3P+4NGBBL8zfchcet3JSuznitrxgASTQ0lGagKaStarDsZ46sNDRXSlIeATM5z57ONEqBv0Uwgq9rIEGYVTuToMxAGPWzG2M51auxxWnw4riJDhg0lB4MJ+BnZjzReMOuW27sGOqUBorbTfGZ/ObJm5D+/wqH0WDl52r6BD7DDLlS0aB3MO/eZzj4oIItRFZF35M57Kw4Rs9b52nY7Jj65ARJ6lTwuE9+ZP4YKQl9B9uf7Mq0b4ty8EIj2w7XKbdQ/C2QrCOifd22sPo3jetrKM6uEzsdsxnB99EG9o/bADX+FDmFKy/PwHo1TIwrMUJxmL1I8g+Yqkhqnbuwd+wWAKA4Vn0fQ4qHpyo8F'

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
