it = 0
def fibonacci(tam_escada):
    cache = []

    def memoize(num):
        seq = 2
        global it

        if num in cache:
            return cache[num]
        
        elif num <= 1:
            it += 1
            return 1, it
        else:
            while seq < tam_escada:

                soma = memoize(num - 1) + memoize(num - 2)
                cache.append(soma)
                return soma
    
    resultado = memoize(tam_escada)
    return resultado[-1]

quantos = int(input("Quantos degraus tem a escada? "))
resul = fibonacci(quantos)
print(resul)
print(it)

