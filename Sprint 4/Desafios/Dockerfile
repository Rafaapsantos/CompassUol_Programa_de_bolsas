# usa a imagem do Python 3.9 com uma versão slim que é mais leve, para reduzir o tamanho da imagem
FROM python:3.9-slim

# copia o arquivo carguru.py do meu diretório local para o diretório /app/ do contêiner
COPY carguru.py /app/

# define o diretório de trabalho dentro do contêiner como /app/
WORKDIR /app/

# configura o comando para executar o arquivo carguru.py com Python quando eu iniciar o contêiner
CMD [ "python", "carguru.py" ]

