def fib(quantos):
    if quantos < 3:
        return 1
    else:
        return fib(quantos - 1) + fib(quantos - 2)

tam = int(input("Qual número da sequência você gostaria de saber? "))
resul = fib(tam)
print(resul)