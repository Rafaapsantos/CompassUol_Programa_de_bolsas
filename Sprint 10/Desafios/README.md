# Desafio 

# Perguntas

Primeiro, vou explorar a seguinte questão:

* Qual foi o ano em que mais filmes de Drama/Romance foram lançados? OK

A partir dela, pretendo expandir a análise com outras perguntas, como:

Incluí mais algumas possíveis perguntas na minha análise.

1. Quais são os 10 filmes mais bem avaliados no gênero Drama/Romance? OK
2. Quais são os 10 atores que mais participaram de filmes de Drama/Romance? 
3. Quais são os 3 filmes mais votados no gênero Drama/Romance?
4. Qual é a média de idade dos atores que atuam em filmes de Drama/Romance?
5. Quais países mais produzem filmes de Drama/Romance? ok
6. Existe alguma correlação entre o país de origem e a popularidade (nota média ou número de votos)?
7. Qual a duração média dos filmes de Drama/Romance? OK
8. Filmes de quais países têm as maiores notas médias?
9. Como a popularidade dos filmes de Drama/Romance varia entre os países de produção?
10. Existe algum padrão entre o idioma original do filme e sua avaliação/popularidade?

Vou detalhar um pouco mais sobre as minhas questões.
1. Essa análise ajuda a identificar características específicas, como direção, enredo e elenco, que fazem um filme ser altamente avaliado. Também pode revelar tendências no gênero, como preferências por épocas ou diretores.

2. Destaca profissionais com carreiras prolíficas no gênero, ajudando a compreender a preferência da indústria cinematográfica por certos artistas e sua relevância nesse contexto.

3. Revela quais filmes tiveram maior popularidade ou impacto, indicando uma possível correlação entre marketing, distribuição e o interesse do público.

4. Ajuda a identificar o perfil demográfico predominante dos atores no gênero e mostra se existe uma faixa etária mais favorecida para papéis nesse tipo de produção.

5. Identifica os líderes globais na produção do gênero, evidenciando a contribuição cultural e regional para dramas e romances.

6. Revela possíveis vieses regionais na avaliação ou consumo de filmes, ajudando a entender como o público responde a produções com base no país de origem.

7. Mostra o padrão típico de duração para o gênero, ajudando na criação de produções que atendam às expectativas do público.

8. Destaca países reconhecidos pela qualidade de suas produções, seja por direção, roteiro ou outros fatores, ajudando a entender a percepção global de excelência no gênero.

9. Pode revelar quais países dominam o gênero e onde há maior aceitação do público.

10. Pode indicar se filmes em certos idiomas têm maior aceitação global ou regional. Também pode revelar se produções em inglês dominam o mercado ou se há espaço para outros idiomas crescerem.

#
Antes de fazer com as configurações no QuickSight, precisei voltar à Sprint 9 para corrigir duas colunas que eu não havia tratado anteriormente. Ajustei essas colunas para garantir que os dados estivessem corretos e bem estruturados antes de utilizá-los na ferramenta de visualização.

[script.py](../Desafios/script.py)

Fiz essa modificação nessa parte para excluir alguns IDs que identifiquei durante a análise no Athena. Isso foi necessário para garantir que os dados estivessem mais limpos e coerentes para a visualização no QuickSight.

![evidencia13](../Evidencias/evidencia13.png)

Esse trecho do código que mudei faz o tratamento de colunas que contêm listas aninhadas dentro do DataFrame no Spark.

![evidencia14](../Evidencias/evidencia14.png)

* A função explode() foi usada para dividir a lista em múltiplas linhas.
* A coluna origin_country contém uma lista de países, cada país será transformado em uma nova linha.
* Isso significa que se um filme tem mais de um país de origem, ele será duplicado para cada país na nova estrutura.

* Na production_countries é uma lista de estruturas (structs) dentro do DataFrame.
* O explode() também divide essa lista em várias linhas, uma para cada país de produção.

* Depois de explodir a coluna production_countries, cada linha contém uma struct com informações como nome do país e código do país (ISO 3166-1).
* Aqui, eu selecionei apenas o código do país (iso_3166_1), substituindo a coluna original.

Por fim, criei uma nova tabela dimensional e a adicionei à tabela fato.

![evidencia15](../Evidencias/evidencia15.png)

Após isso, rodei o código no Glue, executei o crawler e acessei as tabelas para verificar se estava tudo correto.

Depois disso, a primeira coisa que fiz foi criar uma conta no QuickSight, conforme as instruções do desafio.

Após a criação, apareceu uma tela semelhante à da imagem abaixo. Em seguida, cliquei em __Datasets__ e depois em __New Dataset__ para começar a configuração dos dados.

![evidencia1](../Evidencias/evidencia1.png)

Depois de clicar em Athena, dei um nome para o meu data source e continuei com a configuração.

![evidencia2](../Evidencias/evidencia2.png)

![evidencia3](../Evidencias/evidencia3.png)

Após isso, selecionei o database chamado camada_refined e escolhi a tabela fato_filmes. Em seguida, cliquei em Edit/Preview Data para visualizar e editar os dados antes de prosseguir.

![evidencia4](../Evidencias/evidencia4.png)

Então, apareceu uma página informando que eu não tinha permissão para me conectar. 

![evidencia5](../Evidencias/evidencia5.png)

Para resolver isso, fui até o console da AWS, acessei o IAM, cliquei em Roles e pesquisei por QuickSight. Depois, selecionei a role correspondente e cliquei em Add Permissions. Em seguida, adicionei as seguintes políticas necessárias para garantir o acesso adequado.

![evidencia6](../Evidencias/evidencia6.png)

Depois que as permissões foram adicionadas corretamente, a conexão funcionou. Em seguida, cliquei em Add Data -> Datasource, selecionei o nome do Datasource que criei anteriormente e escolhi as tabelas dimensionais para adicionar ao QuickSight.

![evidencia7](../Evidencias/evidencia7.png)

![evidencia8](../Evidencias/evidencia8.png)

![evidencia9](../Evidencias/evidencia9.png)

![evidencia10](../Evidencias/evidencia10.png)

Para estabelecer as relações entre as tabelas, cliquei nas duas bolinhas rosas que aparecem entre elas. Em Join Type, selecionei Inner Join, garantindo que apenas os registros correspondentes fossem mantidos. Em Join Clauses, escolhi os IDs correspondentes para conectar as tabelas corretamente. Repeti esse processo para todas as tabelas dimensionais e a tabela fato.

![evidencia11](../Evidencias/evidencia11.png)

Depois ficou assim 

![evidencia12](../Evidencias/evidencia12.png)


