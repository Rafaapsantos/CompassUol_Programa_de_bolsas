# Sprint 6
## Desafio
Esse desafio consistia em elaborar perguntas para realizar a análise ao longo das próximas sprints e também em fazer o upload dos arquivos movies e series para o bucket criado na AWS.

[Desafio](../Sprint%206/Desafios/)

# Exercícios 
### Exercício - LAB AWS Athena 

Primeiro, verifiquei se o arquivo nomes.csv estava presente no meu bucket.

![evidencia1](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia1.png)

Em seguida, analisei o arquivo para entender melhor os dados contidos nele.

Depois disso, criei uma pasta chamada queries dentro do bucket.

![evidencia2](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia2.png)

Em seguida, configurei o local onde os resultados das consultas seriam armazenados.

![evidencia3](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia3.jpeg)

Depois, escrevi e executei o comando para criar o meu banco de dados.

![evidencia4](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia4.png)

Por fim, na lista Database, selecionei o banco de dados recém-criado para defini-lo como meu banco de dados atual.

![evidencia5](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia5.png)

Em seguida, elaborei a query para criar a tabela no meu banco de dados e a executei.

![evidencia6](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia6.jpeg)

![evidencia7](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia7.png)

Depois, testei os dados utilizando uma consulta específica.
![evidencia8](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia8.png)

Essa é a resposta:

![evidencia9](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia9.png)

Por fim, criei uma query que lista os 3 nomes mais usados em cada década, desde 1950 até os dias atuais. O resultado dessa consulta está armazenado na pasta exercicios, e localizei a resposta acessando a pasta queries do meu bucket.

![evidencia10](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia10.jpeg)

A resposta é essa:

[Resposta](../Sprint%206/Exercicios/Athena/3_nomes_mais_usado_decada.csv)

##
### Exercício - LAB AWS Lambda

Primeiro, criei uma função no AWS Lambda.

![evidencia11](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia11.png)

Em seguida, substituí o código no arquivo lambda_function.py e cliquei em Deploy.

![evidencia12](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia12.png)

Realizei o teste conforme solicitado e, de fato, ocorreu um erro.

Criei o arquivo Dockerfile conforme solicitado e executei todos os comandos indicados. Ao final, obtive dois arquivos: Dockerfile e minha-camada-pandas.zip. 

[Dockerfile](../Sprint%206/Exercicios/Lambda/Dockerfile)

[minha-camada-pandas.zip](../Sprint%206/Exercicios/Lambda/minha-camada-pandas.zip)

Em seguida, realizei o upload do arquivo minha-camada-pandas.zip para dentro do bucket.

![evidencia13](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia13.png)

Em seguida, criei a camada conforme solicitado. Depois, adicionei a camada e, por fim, realizei novos testes e o exercício foi concluído com sucesso.

![evidencia14](../Sprint%206/Evidencias/Evidencia_Exercicios/evidencia14.png)

##

## Certificado 
[Certificado- AWS Skill Builder - Serverless Analytics](../Sprint%206/Certificados/Certificado_AWS_Serverless_Analytics.jpg)

[Certificado- AWS Skill Builder - Introduction to Amazon Athena](../Sprint%206/Certificados/Certificado_AWS_Introduction_Amazon_Athena.jpg)

[Certificado- Getting Started with Amazon Redshift](../Sprint%206/Certificados/Certificado_AWS_Amazon_Redshift.jpg)

[Certificado- AWS Skill Builder - Fundamentals of Analytics on AWS – Part 1](../Sprint%206/Certificados/Certificado_AWS_Fundamentals_Analytics_1.jpg)

[Certificado- AWS Skill Builder - Fundamentals of Analytics on AWS – Part 2](../Sprint%206/Certificados/Certificado_AWS_Fundamentals_Analytics_2.jpg)

[Certificado- AWS Skill Builder - Amazon EMR Getting Started](../Sprint%206/Certificados/Certificado_AWS_Amazon_EMR.jpg)

[Certificado- AWS Skill Builder - Amazon QuickSight - Getting Started](../Sprint%206/Certificados/Certificado_AWS_Amazon_QuickSight.jpg)

[Certificado- AWS Skill Builder - Best Practices for Data Warehousing with Amazon Redshift](../Sprint%206/Certificados/Certificado_AWS_Data_Warehousing_Amazon_Redshift.jpg)

[Certificado- AWS Skill Builder - AWS Glue Getting Started](../Sprint%206/Certificados/Certificado_AWS_Glue.jpg)

## Opnião:
O que mais gostei nesta sprint foram os exercícios, que achei bem interessantes, pois proporcionam um ótimo aprendizado. Sobre o desafio, achei bem tranquilo e não tive dificuldades em executá-lo. A única coisa que não gostei muito foi a quantidade de cursos que precisava assistir. 

## O que aprendi?
1. Fundamentals of Analytics on AWS – Part 1
* Visão geral de analytics
* Visão geral de machine learning (ML)
* Como identificar desafios com analytics
* Armazenamento de dados e os desafios de volume
* Estrutura e tipos de dados e os desafios de variedade
* Processamento de dados e os desafios de velocidade
* Limpeza e transformação de dados, e os desafios de veracidade
* Relatórios e business intelligence, e os desafios de valor
* Produtos da Amazon Web Services (AWS) para desafios com analytics

2. Fundamentals of Analytics on AWS – Part 2
* Introdução aos data lakes 
* Introdução ao data warehousing 
* Introdução à arquitetura de dados moderna 
* Serviços da AWS para arquitetura de dados moderna 
* Casos de uso comuns 
* Arquiteturas de referência 

3. Serverless Analytics
* Como sintetizar diferentes dados usando o poder de ferramentas como AWS IoT Analytics, Amazon Cognito, AWS Lambda e Amazon SageMaker, entre outras.
* Agregar, processar, armazenar e disponibilizar dados úteis de formas inovadoras e poderosas.

4. Introduction to Amazon Athena
* Serviço Amazon Athena junto com uma visão geral do ambiente operacional.
* Etapas básicas da implementação do Amazon Athena

5. AWS Glue Getting Started
* O que o AWS Glue faz?
* Quais problemas o AWS Glue resolve?
* Quais são os benefícios do AWS Glue?
* Qual é o mecanismo de integração de dados suportado pelo AWS Glue?
* Como o AWS Glue é usado para arquitetar uma solução de nuvem?
* Quais são os casos de uso típicos do AWS Glue?
* O que mais devo ter em mente ao usar o AWS Glue?
* Quanto custa a AWS?
* Quais são os conceitos técnicos básicos que devo saber sobre o AWS Glue Studio?
* Como faço para rastrear, catalogar e executar ETL em meus dados usando o AWS Glue?
* Vídeo tutorial do Glue Studio
* Quais são os conceitos técnicos básicos que devo saber sobre o AWS Glue DataBrew?
* Como faço o perfil dos meus dados, detecto PII e transformo meus dados usando o AWS Glue DataBrew?

6. Amazon EMR Getting Started
* Introdução ao Amazon EMR
* Arquitetura e casos de uso sem servidor do Amazon EMR
* Arquitetura e casos de uso do cluster Amazon EMR
* Como criar recursos da AWS para uso com o Amazon EMR Serverless
* Como executo um trabalho do Spark no Amazon EMR Serverless
* Como faço para limpar os recursos sem servidor do Amazon EMR
* Como criar recursos da AWS para uso com o Amazon EMR
* Como criar um Amazon EMR no cluster EC2
* Como criar um Amazon EMR Studio
* Como criar um espaço de trabalho do Amazon EMR
* Como executo um trabalho do Spark com o Amazon EMR Studio Notebook
* Como faço para limpar os recursos do Amazon EMR

7. Getting Started with Amazon Redshift
* Entender como o Amazon Redshift funciona
* Familiarizar-se com os conceitos técnicos do Amazon Redshift
* Listar casos de uso típicos para o Amazon Redshift
* Especificar o que é necessário para implementar o Amazon Redshift em um cenário do mundo real
* Reconhecer quais são os benefícios do Amazon Redshift
* Explicar a estrutura de custos do Amazon Redshift
* Usar o Amazon Redshift no console de gerenciamento da AWS

8. Best Practices for Data Warehousing with Amazon Redshift
* Implementação de um data warehouse usando o Amazon Redshift
* Design básico de tabelas
* Armazenamento de dados
* Técnicas de ingestão de dados 
* Gerenciamento de workload
* Efeito do dimensionamento de nó e de cluster

9. Amazon QuickSight - Getting Started
* Introdução ao QuickSight
* Arquitetura e Casos de Uso
* Como criar um conjunto de dados do QuickSight?
* Como criar uma análise QuickSight?
* Como personalizar o QuickSight usando temas?
* Como publicar um painel do QuickSight?
* Como usar o QuickSight Q para fazer perguntas em linguagem natural?