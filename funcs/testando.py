import time
import pandas as pd

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
            while seq <= tam_escada:

                soma = memoize(num - 1) + memoize(num - 2)
                cache.append(soma)
                return soma
    
    resultado = memoize(tam_escada)
    return resultado[-1]

# Função de medição de tempo
def tempo_exec(func, *args):
    inicio = time.time()
    resultado = func(*args)
    tempo_decorrido = time.time() - inicio
    return tempo_decorrido

# Implementando o pandas para imprimir os valores de tempo de execução para diferentes soluções e comparação de processamento.
# Aqui eu já até diminui o valor da lista porque a execução já tava com 3 minutos na primeira execução ;-;
valores = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
resultados_com = []
formas_de_subir = []
primeira_exec = []
segunda_exec = []

for i in valores:

    #1° execução
    tempo_com_memoization = tempo_exec(fibonacci, i)
    primeira_exec.append(tempo_com_memoization) #Aparentemente, é um memoize, mas não. Então vai rodar com o mesmo tempo de uma função recursiva sem memoization.

    #2° execução
    tempo_com_memoization = tempo_exec(fibonacci, i)
    segunda_exec.append(tempo_com_memoization) #Aqui já vai rodar mais rápido pq os dados estão decorados.

dados = {'Valores': valores,
         '1° execução': primeira_exec,
         '2° execução': segunda_exec}

dados_tabelados = pd.DataFrame(dados)
print(dados_tabelados)