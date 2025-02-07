# Desafio 

# Perguntas

Primeiro, vou explorar a seguinte questão:

* Qual foi o ano em que mais filmes de Drama/Romance foram lançados?

A partir dela, pretendo expandir a análise com outras perguntas, como:

Incluí mais algumas possíveis perguntas na minha análise.

1. Quais são os 10 filmes mais bem avaliados no gênero Drama/Romance?
2. Quais são os 10 atores que mais participaram de filmes de Drama/Romance?
3. Quais são os 3 filmes mais votados no gênero Drama/Romance?
4. Qual é a média de idade dos atores que atuam em filmes de Drama/Romance?
5. Quais países mais produzem filmes de Drama/Romance?
6. Existe alguma correlação entre o país de origem e a popularidade (nota média ou número de votos)?
7. Qual a duração média dos filmes de Drama/Romance?
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
### Modelagem Multidimencional
A primeira coisa que fiz para executar este desafio foi organizar a modelagem multidimensional. Para isso, utilizei o Athena para consultar minhas tabelas JSON e CSV, verificando quais colunas estavam disponíveis e separando as informações necessárias para a modelagem. 

![evidencia1](../Evidencias/evidencia1.png)

![evidencia2](../Evidencias/evidencia2.png)

Em seguida, usei o Notion para anotar a estrutura da tabela fato e das tabelas dimensão.

Antes de anotar no Notion, revisei as colunas que trouxe para a camada Trusted e decidi excluir algumas delas do diagrama e depois vou excluí-las para a camada refined. Removi a coluna budget, pois a maioria dos filmes não tinha esse valor preenchido. Também excluí a coluna tituloPrincipal, já que o tituloOriginal era suficiente para a análise. Além disso, descartei a coluna personagem, pois no início do processo eu já havia removido as linhas duplicadas que listavam todos os personagens de um filme. Analisar apenas um personagem por filme não faria sentido, então optei por excluí-la.

![evidencia3](../Evidencias/evidencia3.png)

Depois disso, utilizei o draw.io, um programa com o qual já tenho familiaridade, para criar o diagrama conforme as instruções do desafio.

![evidencia4](../Evidencias/evidencia4.png)

Para as ligações entre as tabelas, utilizei a relação __"1 optional to many mandatory"__, onde:

* Do lado do "1 optional", uma ocorrência da entidade __A__ pode ou não estar associada à entidade __B__, tornando sua participação na relação opcional.
* Do lado do "many mandatory", cada ocorrência da entidade __B__ deve estar associada a pelo menos uma ocorrência da entidade __A__, podendo estar vinculada a várias.

### Código

