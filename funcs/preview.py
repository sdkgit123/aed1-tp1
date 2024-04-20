import time
import pandas as pd

it1 = 0
it2 = 0


# Adaptação do código def_fib_com_recursao.py
def sem_memoize(quantos):
    global it1
    if quantos <= 1:
        it1 += 1
        return 1
    else:
        it1 += 1
        return sem_memoize(quantos - 1) + sem_memoize(quantos - 2)


# Função de memoization (def_new_memoize.py)
def memoize(tam_escada, cache):
    global it2
    if cache is None:
        it2 += 1
        cache = [1] * (tam_escada + 1)  # Inicializa a lista com 6 elementos todos com +1
    if cache[tam_escada] != 1:
        it2 += 1
        return cache[tam_escada]
    elif tam_escada <= 1:
        it2 += 1
        return 1
    else:
        it2 += 1
        cache[tam_escada] = memoize(tam_escada - 1, cache) + memoize(tam_escada - 2, cache)
        return cache[tam_escada]


# Função de medição de tempo (def_time.py)
def tempo_exec(func, *args):
    inicio = time.time()
    resultado = func(*args)  # Passar o valor da função
    tempo_decorrido = time.time() - inicio
    return tempo_decorrido

def iteracoesnm(func, *args):
    global it1
    if it1 == 0:
        resul = func(*args)
    else:
        it1 = 0
        resul = func(*args)
    return it1

def iteracoesm(func, *args):
    global it2
    if it2 == 0:
        resul = func(*args)
    else:
        it2 = 0
        resul = func(*args)
    return it2


# Implementando o pandas para printar os valores de tempo de execução para diferentes soluções e comparação de processamento.
valores = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
resultados_com = []
resultados_sem = []
formas_de_subir = []
iteracoessem = []
iteracoescom = []

for i in valores:
    semmemoit = iteracoesnm(sem_memoize, i)
    commemoit = iteracoesm(memoize, i, None)
    iteracoessem.append(semmemoit)
    iteracoescom.append(commemoit)
    tempo_com_memoization = tempo_exec(memoize, i, None)
    resultados_com.append(tempo_com_memoization)
    tempo_sem_memoization = tempo_exec(sem_memoize, i)
    resultados_sem.append(tempo_sem_memoization)
    formas = memoize(i, None)
    formas_de_subir.append(formas)


dados = {'Formas': formas_de_subir,
         'Valores': valores,
         'Execução sem memoization': resultados_sem,
         'Execução com memoization:': resultados_com,
         'Iterações sem memoization:': iteracoessem,
         'Iterações com memoization:': iteracoescom
         }

dados_tabelados = pd.DataFrame(dados)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(dados_tabelados.to_string(index=False))

