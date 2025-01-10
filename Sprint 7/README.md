# Sprint 7
## Desafio
A segunda entrega do desafio final é uma das mais importantes. Ela consistia em capturar os dados do TMDB utilizando o AWS Lambda para complementar as informações de filmes e séries que foram carregadas na etapa 1.

[Desafio](../Sprint%207/Desafios/)

# Exercícios 
### Exercício - LAB AWS GLUE 
A primeira coisa que fiz foi criar as pastas no bucket e fazer o upload do arquivo nomes.csv.

![evidencia1](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia1.png)

Em seguida, continuei seguindo os passos disponibilizados no curso da Udemy.

![evidencia2](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia2.png)

Depois, no Glue, segui as instruções conforme orientado.

![evidencia3](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia3.png)

![evidencia4](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia4.png)

Passei então para o AWS Lake Formation, onde também segui os passos indicados.

![evidencia5](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia5.png)

Voltei ao Glue e continuei seguindo os passos para concluir o processo.

![evidencia7](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia7.png)

![evidencia6](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia6.png)

![evidencia8](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia8.png)

![evidencia19](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia19.png)

Depois eu fiz o script python que foi pedido

[script.py](../Sprint%207/Exercicios/AWS%20GLUE/script.py)

Aqui eu forneci os parâmetros necessários

![evidencia9](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia9.png)

Rodei e esses foram os resultados 

O schema do dataframe

![evidencia20](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia20.png)

Contagem de linhas

![evidencia21](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia21.png)

Contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo

![evidencia22](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia22.png)

Qual foi o nome feminino com mais registros e em que ano ocorreu

![evidencia23](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia23.png)

Qual foi o nome masculino com mais registros e em que ano ocorreu

![evidencia24](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia24.png)

O total de registros (masculinos e femininos) para cada ano presente no dataframe

![evidencia25](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia25.png)

Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3

![evidencia26](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia26.png)

![evidencia27](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia27.png)

![evidencia28](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia28.png)

##
### Exercício - TMDB

Segui todas as etapas indicadas no curso da Udemy e me cadastrei no TMDB. Testei para garantir que estava tudo funcionando corretamente.
OBS: Por segurança, apaguei minha chave de acesso.

![evidencia10](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia10.jpeg)

![evidencia11](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia11.jpeg)

Escrevi o código que foi disponibilizado e o executei usando o comando:
python script.py.

[script.py](../Sprint%207/Exercicios/TMDB/script.py)

![evidencia12](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia12.png)

##
### Exercício - Apache Spark - Contador de Palavras
Primeiro, executei o comando abaixo para baixar a imagem do Docker:
![evidencia13](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia13.png)

Depois, rodei este comando para criar e inicializar o contêiner no modo interativo, com mapeamento da porta 8888, para acessar o JupyterLab e testar antes:

![evidencia14](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia14.png)

Em seguida, testei o código no Jupyter e funcionou certinho. Então, executei o comando abaixo para verificar o ID do contêiner:

![evidencia15](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia15.png)

OBS: Todos os comandos acima foram executados diretamente no terminal do VS Code.

Depois disso, abri um terminal no WSL e executei o comando abaixo para acessar o terminal interativo do Spark:

![evidencia16](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia16.png)

Em seguida, rodei os comandos abaixo para contar a quantidade de palavras no arquivo README.md (usei o README de apresentação, que foi o primeiro que fizemos):

![evidencia17](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia17.png)

Esses são os comandos utilizados:
[comandos_execução](../Sprint%207/Exercicios/Apache%20Spark/comandos_execução.txt)

E este foi o resultado: 
![evidencia18](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia18.png)

Também disponibilizei um arquivo .txt contendo a resposta:

[resposta](../Sprint%207/Exercicios/Apache%20Spark/resultado.txt)

## Opnião:
Gostei da sprint, mas tive algumas dificuldades com o Spark, principalmente na parte de instalação. O exercício do Glue também me demandou bastante tempo, pois eu estava cometendo algum erro que fazia com que sempre desse 'failed' ao rodar. No entanto, perguntei aos colegas e consegui resolver.

## O que aprendi?
1. Formação Spark com Pyspark
* Como instalar spark
* RRD, Dataset e Dataframe
* Exportar e importar dados
* Spark SQL
* Criar aplicações
* Otimização
* Spark com jupter
* Spark UI