#EXE 004 - Escreva um programa para pedir um número e em seguida o nome. Exiba o nome (uma letra de cada vez em cada linha) e repita isso para o número de vezes que ele digitou.
nome = input("Digite seu nome: ")
num = int(input("Digite um numero: "))
for i in range(num):
    for letra in nome:
        print(letra)