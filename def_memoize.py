def fibonacci(tam_escada):
    cache = {}

    def memoize(num):

        if num in cache:
            return cache[num]
        
        elif (num <= 1):
            resultado = 1
            cache[num] = resultado
            return resultado
        else: 
            resultado = memoize(num-1) + memoize(num-2)
            cache[num] = resultado
            return resultado

            
    return memoize(tam_escada)