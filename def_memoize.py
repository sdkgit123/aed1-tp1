def fibonacci(tam_escada):
    cache = {}
    it = 0

    def memoize(num, it):

        soma = 0
        seq = 2

        if num in cache:
            return cache[num]
        
        elif (num <= 1):
            it += 1
            return 1, it
        else: 
            while seq < tam_escada:

                soma = memoize(num - 1, it) + memoize(num - 2, it)
                cache[num] = soma
                return soma
    
    resultado = memoize(tam_escada, it)
    return resultado