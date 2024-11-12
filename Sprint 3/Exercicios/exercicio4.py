for numero in range(2, 101):
    numero_primo = True
    i = 2

    while i * i <= numero:
        if numero % i == 0:
            numero_primo = False
            break
        i += 1

    if numero_primo:
        print(numero)
