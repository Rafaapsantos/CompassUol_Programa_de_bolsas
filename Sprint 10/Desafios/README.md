# Desafio 

# Perguntas

Fiz algumas alterações nas perguntas, mas as seguintes questões foram respondidas na minha análise:

1. Existe algum país de origem que tenha uma correlação direta com a alta popularidade dos filmes, ou a popularidade é mais distribuída entre os países?
2. Qual a duração média dos filmes de Drama/Romance?
3. Quais países mais produzem filmes de Drama/Romance?
4. Quais são os 10 filmes mais bem avaliados no gênero Drama/Romance?
5. Filmes em quais idiomas tendem a ser mais populares?
6. Há algum padrão ou agrupamento na duração dos filmes de Drama/Romance, como picos em certas faixas de tempo?
7. Qual é o continente com a maior diversidade de idiomas nos filmes?
8. Os filmes mais longos tendem a receber notas mais altas, ou há exceções notáveis?
9. Qual é a média de idade dos atores que atuam em filmes de Drama/Romance?
10. Qual foi o ano em que mais filmes de Drama/Romance foram lançados?

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

Para criar o dashboard, a primeira coisa que fiz foi acessar o site [Color Hunt](https://colorhunt.co/) e escolher uma paleta de cores que combinasse com o meu tema, que é Romance/Drama. Depois de definir a paleta, fui até o QuickSight, cliquei em Edit -> Themes -> My Themes e criei um tema personalizado com as cores selecionadas.
Também criei uma imagem com um título no Canva para adicionar ao meu dashboard, deixando a apresentação mais visual e organizada.

Antes de começar a criar os gráficos, criei alguns campos calculados para facilitar a visualização dos dados:

* idade_atores: calculei a idade que os atores tinham quando participaram do filme.
![evidencia16](../Evidencias/evidencia16.png)
* idioma_continente: agrupei os idiomas por continente.
![evidencia18](../Evidencias/evidencia18.png)
* idioma: substituí as siglas dos idiomas pelos seus respectivos nomes para facilitar a compreensão, já que eu não conhecia todas as siglas.
![evidencia17](../Evidencias/evidencia17.png)
* países: substituí as siglas dos países pelos seus nomes completos, tornando a visualização mais intuitiva.
![evidencia19](../Evidencias/evidencia19.png)

Agora vou falar sobre os meus gráficos. Para cada um, vou apresentar a pergunta analisada, uma breve explicação e um print do gráfico que criei para responder à questão.

1. Existe algum país de origem que tenha uma correlação direta com a alta popularidade dos filmes, ou a popularidade é mais distribuída entre os países?

* Identificar se há um ou mais países que dominam a produção de filmes populares em Drama/Romance ou se há uma distribuição mais equilibrada. Isso pode indicar tendências culturais e a força da indústria cinematográfica de certos países no gênero.

![evidencia29](../Evidencias/evidencia29.png)

2. Qual a duração média dos filmes de Drama/Romance?

* Ter uma noção da duração típica desses filmes pode ajudar a entender o padrão de consumo do público. Filmes muito curtos podem indicar histórias mais simples, enquanto filmes mais longos podem sugerir tramas mais profundas e elaboradas.

![evidencia21](../Evidencias/evidencia21.png)

3. Quais países mais produzem filmes de Drama/Romance?

* Descobrir os países que mais investem nesse gênero pode mostrar onde há uma maior demanda ou tradição em narrativas dramáticas e românticas. Isso pode revelar influências culturais e cinematográficas regionais.

![evidencia22](../Evidencias/evidencia22.png)

4. Quais são os 10 filmes mais bem avaliados no gênero Drama/Romance?

* Compreender quais filmes são mais bem avaliados pode revelar padrões em elementos como roteiro, elenco e direção que os tornam marcantes para o público e crítica. Isso também pode ajudar a identificar diretores, roteiristas e atores mais influentes no gênero.

![evidencia23](../Evidencias/evidencia23.png)

5. Filmes em quais idiomas tendem a ser mais populares?

* Avaliar a relação entre idioma e popularidade pode indicar se há um viés para determinadas línguas, como inglês e francês, ou se filmes em idiomas menos falados também conseguem alcançar grande sucesso. Isso pode estar ligado à acessibilidade e distribuição global.

![evidencia24](../Evidencias/evidencia24.png)

6. Há algum padrão ou agrupamento na duração dos filmes de Drama/Romance, como picos em certas faixas de tempo?

*  Identificar se há faixas de tempo mais comuns (ex.: 90-110 min, 120-140 min) pode mostrar preferências do público e dos estúdios em relação à duração ideal para esse tipo de filme. Picos de frequência podem indicar o formato mais aceito para manter o engajamento do espectador.

![evidencia30](../Evidencias/evidencia30.png)

7. Qual é o continente com a maior diversidade de idiomas nos filmes?

*  Avaliar a diversidade linguística nos filmes por continente pode revelar a riqueza cultural das produções cinematográficas e quais regiões investem mais em produções multilíngues. Isso também pode apontar para mercados mais abertos à diversidade cultural.

![evidencia25](../Evidencias/evidencia25.png)

8. Os filmes mais longos tendem a receber notas mais altas, ou há exceções notáveis?

* Descobrir se há uma relação entre a duração e a nota dos filmes pode indicar se filmes mais longos são percebidos como mais profundos e complexos (e, portanto, bem avaliados) ou se há um ponto de saturação onde o tempo de exibição prejudica a experiência do espectador.

![evidencia28](../Evidencias/evidencia28.png)

9. Qual é a média de idade dos atores que atuam em filmes de Drama/Romance?

* Avaliar a idade média dos atores pode indicar padrões de escolha de elenco para esse gênero. Pode ser que existam faixas etárias predominantes, como jovens para romances adolescentes ou atores mais experientes para dramas profundos.

![evidencia26](../Evidencias/evidencia26.png)

10. Qual foi o ano em que mais filmes de Drama/Romance foram lançados?

*  Identificar o pico de lançamentos pode indicar tendências históricas no cinema, como períodos de alta produção para esse gênero. Isso pode estar relacionado a movimentos cinematográficos, mudanças na demanda do público ou avanços na indústria do entretenimento.

![evidencia27](../Evidencias/evidencia27.png)

E este é o dashboard completo, reunindo todas as visualizações e análises que realizei.

![evidencia31](../Evidencias/evidencia31.png)

[Dashboard](../Desafios/Dashboard_movies_romance_drama.pdf)

