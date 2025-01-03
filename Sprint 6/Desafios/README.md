# Desafio 

## Perguntas 
1. Qual foi o número de artistas falecidos por década no gênero Drama/Romance?
2. Quais são os 10 filmes mais bem avaliados no gênero Drama/Romance?
3. Qual foi o ano em que mais filmes de Drama/Romance foram lançados?
4. Qual é a quantidade de filmes de Drama/Romance lançados por ano?
5. Quais artistas têm mais personagens associados a filmes do gênero Drama/Romance?
6. Quais são os 10 atores que mais participaram de filmes do gênero Drama/Romance?
7. Quais são os 3 filmes do gênero Drama/Romance mais votados?
8. Qual é o filme mais antigo do gênero Drama/Romance, considerando a data de lançamento?

Antes de tudo, analisei os arquivos CSV fornecidos e, com base nessa análise, criei as perguntas.

### _Lembrete_: estou utilizando variáveis dentro dos scripts, pois não consegui cadastrar minhas credenciais da AWS utilizando o comando aws configure
Depois eu criei um código simples com o objetivo de criar o bucket necessário para os desafios das próximas sprint.

Aqui está uma imagem do bucket na AWS, junto com o link para acessá-lo.

__Importante__: Para testar o script, é necessário adicionar as credenciais da AWS. No entanto, elas foram removidas do arquivo por questões de segurança.

![evidencia10](../Evidencias/Evidencias_desafio/evidencia13.png)

[Link para o script que cria o bucket](../Desafios/criar_bucket.py)

Em seguida, criei o arquivo enviar_arquivos.py para enviar os arquivos [movies.csv](../Desafios/dados/movies.csv) e [series.csv](../Desafios/dados/series.csv) para o bucket que foi criado anteriormente. 
Segue o link para o arquivo:
[enviar_arquivos.py](../Desafios/enviar_arquivos.py)

Depois disso, criei o arquivo Dockerfile e o arquivo docker-compose.yml. O docker-compose.yml é um arquivo de configuração que permite definir e gerenciar vários contêineres Docker de forma organizada, especificando suas imagens, volumes, redes e outras dependências em um único local.
Segue o link para os arquivos:
[Dockerfile](../Desafios/Dockerfile)

[docker-compose.yml](../Desafios/docker-compose.yml)

Antes de começar a executar os comandos necessários, abri o Docker Desktop, já que, se tentar executar qualquer comando Docker sem que ele esteja inicializado, ocorre um erro e coloquei as minhas credenciais no script python.

Para executar os comandos Docker, cliquei com o botão direito do mouse sobre o diretório onde estão o arquivo Dockerfile e enviar_arquivos.py. Isso garantiu que os comandos fossem executados no local correto, evitando erros relacionados ao caminho do arquivo.

Para criar a imagem Docker, utilizei o seguinte comando:

![evidencia14](../Evidencias/Evidencias_desafio/evidencia14.gif)

Após criar a imagem, usei o comando abaixo para verificar se a imagem foi criada corretamente:

![evidencia16](../Evidencias/Evidencias_desafio/evidencia16.gif)

Esse comando lista todas as imagens Docker disponíveis no meu sistema, permitindo confirmar que a imagem imagem-desafio6 foi criada com sucesso e está presente.

Depois de confirmar que a imagem desafio foi criada com sucesso, utilizei o comando:

![evidencia15](../Evidencias/Evidencias_desafio/evidencia15.gif)

Esse comando cria e executa um container com base na imagem imagem-desafio6.

Após executar o contêiner, acessei meu bucket para verificar se tudo estava correto.

![evidencia17](../Evidencias/Evidencias_desafio/evidencia17.gif)




