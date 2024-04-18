import sys 

quantos = int(input("Qual número da sequência você gostaria de saber? "))

um = 1
dois = 1
seq = 2
soma = 0

if quantos == 1 or quantos == 2:
    print(um)
    sys.exit() #Função de tratamento de erro?
else:
    while seq < quantos:
        soma = um + dois
        um = dois
        dois = soma
        seq += 1

print(soma)