#1° passo é abrir o arquivo actors, armazenar ele em uma variável pra ficar mais de usar e ler o conteúdo do 
# arquivo

with open('actors.csv', 'r') as arquivo:
    conteudo = arquivo.readlines()
    print(conteudo)


#2° passo é fazer uma mudança no nome da linha 5, porque tem uma vírgula que atrapalha quando tenta fazer a 
# etapa 1

count = 0
for i in conteudo:
    linhas = i.strip().split(',')
    if count == 5:
        linhas[0] = 'Robert Downey JR'
        del linhas[1]
        conteudo[count] = ','.join(linhas)
    count += 1

#3° passo é fazer o código para apresentar o ator/atriz com maior número de filmes

maior_quantidade = 0
ator = ''

for i in conteudo[1:]:
    linhas = i.strip().split(',')
    num_filmes = int(linhas[2])

    if num_filmes > maior_quantidade:
        maior_quantidade = num_filmes
        ator = linhas[0]


ator_com_mais_filme = f'O ator/atriz com maior numero de filmes é {ator} com um total de {maior_quantidade} filmes'

#4° passo é colocar o resultado do passo 3 no arquivo etapa-1.txt 

with open("etapa-1.txt", "w", encoding='utf-8') as etapa1:
    etapa1.write(ator_com_mais_filme)

#5° passo é fazer o código para apresentar a média de receita de bilheteria bruta dos principais filmes

soma = 0
for i in conteudo[1:]:
    linhas = i.strip().split(',')
    soma += float(linhas[5])

media = round(soma / len(conteudo[1:]),2)

media_receita_bilheteria = f'A média de receita de bilheteria bruta dos principais filmes, considerando todos os atores é de {media}'

#6° passo é colocar o resultado do passo 5 no arquivo etapa-2.txt

with open("etapa-2.txt", "w", encoding='utf-8') as etapa2:
    etapa2.write(media_receita_bilheteria)

#7° passo é fazer o código para apresentar o ator/atriz com a maior média de receita de bilheteria bruta por 
# filme 

maior_media = 0
nome_ator_maior = ""

for i in conteudo[1:]:
    linhas = i.strip().split(',')
    nome_ator = linhas[0]
    if float(linhas[3]) > maior_media:
        maior_media = float(linhas[3])
        nome_ator_maior = nome_ator
        
nome_ator_maior_media= f' O ator/atriz com maior média de receita de bilheteria bruta por filme foi {nome_ator_maior} com uma media de: {maior_media}'

#8° passo é colocar o resultado do passo 7 no arquivo etapa-3.txt

with open("etapa-3.txt", "w", encoding='utf-8') as etapa3:
    etapa3.write(nome_ator_maior_media)

# 9° passo é fazer o código para apresentar a contagem de aparições que dos filmes, listando-os pela quantidade de 
# vezes que estão presentes

filmes= {}
filmes_procurados = ''

for i in conteudo[1:]:
    linhas = i.strip().split(',')
    filmes_procurados = linhas[4]
    if filmes_procurados in filmes:
        filmes[filmes_procurados] +=1
    else:
        filmes[filmes_procurados] = 1

filmes = sorted(filmes.items(), key=lambda x: (-x[1], x[0]))

contagem_aparicao = ''
count = 1
for filme, quantidade in filmes:
    contagem_aparicao += f'{count} - O filme {filme} aparece {quantidade} vez(es) no dataset \n'
    count +=1

# 10° passo é colocar o resultado do passo 9 no arquivo etapa-4.txt

with open("etapa-4.txt", "w", encoding='utf-8') as etapa4:
    etapa4.write(contagem_aparicao)

# 11° passo é fazer o código para apresentar a lista dos atores ordenada pela receita bruta de bilheteria dos filmes 
# em ordem decrescente

ator_receita = {}

for i in conteudo[1:]:
     linhas = i.strip().split(',')
     nome_ator = linhas[0]
     ator_receita[nome_ator] = float(linhas[1])

ator_receita = sorted(ator_receita.items(), key=lambda x: (-x[1]))

atores_receita_bruta = ''
for nome_do_ator, receita_total in ator_receita:
    atores_receita_bruta += f'{nome_do_ator} - {receita_total}\n'

# 12° passo é colocar o resultado do passo 11 no arquivo etapa-5.txt

with open("etapa-5.txt", "w", encoding='utf-8') as etapa5:
    etapa5.write(atores_receita_bruta)