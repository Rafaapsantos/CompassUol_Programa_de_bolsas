# usa a imagem do Python 3.9 com uma versão slim que é mais leve, para reduzir o tamanho da imagem
FROM python:3.9-slim

# define o diretório de trabalho dentro do contêiner como /app/
WORKDIR /app

# copia os arquivo para o diretório /app/ do contêiner
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir boto3 python-dotenv pandas

# Defina o comando padrão para execução 
CMD ["python", "enviar_arquivos.py"]