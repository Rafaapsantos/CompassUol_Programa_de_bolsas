import hashlib

controle = True

while controle:
    print('1 - Sair do Script\n2 - Inserir string')
    operacao = input('Digite o código da operação desejada: ')
    if operacao == '2':
        string = input('Digite uma palavra para mascarar: ')
        hash = hashlib.sha1(string.encode())
        print(hash.hexdigest())
    elif operacao == '1':
        controle = False
    else:
        print('Código não aceito, digite novamente!')
        