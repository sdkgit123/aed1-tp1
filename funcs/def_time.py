import time

#*args passa o argumento da função que precisa ter seu tempo de execução
def tempo_exec(func, *args): 
    inicio = time.time()
    resultado = func(*args) #Passar o valor da função
    tempo_decorrido = time.time() - inicio
    print(f"Tempo de execução: {tempo_decorrido:.5f} segundos")
    return resultado