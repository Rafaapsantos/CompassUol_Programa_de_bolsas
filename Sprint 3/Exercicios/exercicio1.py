from datetime import datetime

nome = 'Rafaela'
idade = 19

idade_para_100 = 100 - idade
data_100_anos = datetime.now().year + idade_para_100

print(data_100_anos)