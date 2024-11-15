def funcao(*args, **kwargs):
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(value)

funcao(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)