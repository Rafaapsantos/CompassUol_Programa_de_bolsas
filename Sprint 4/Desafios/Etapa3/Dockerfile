# usa a imagem do Python 3.9 com uma versão slim que é mais leve, para reduzir o tamanho da imagem
FROM python:3.9-slim

# copia o arquivo script.py do meu diretório local para o diretório /app/ do conteiner
COPY script.py /app/

# define o diretório de trabalho dentro do container como /app/
WORKDIR /app/

# configura o comando para executar o arquivo script.py com Python quando eu iniciar o conteiner
CMD [ "python", "script.py" ]

