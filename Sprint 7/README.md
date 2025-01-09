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

Depois eu fiz o script python que foi pedido

[script.py](../Sprint%207/Exercicios/AWS%20GLUE/script.py)

Aqui eu forneci os parâmetros necessários

![evidencia9](../Sprint%207/Evidencias/Evidencias_exercicios/evidencia9.png)

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