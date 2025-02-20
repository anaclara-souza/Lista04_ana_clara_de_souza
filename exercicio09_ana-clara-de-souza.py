#EXE 009 - Faça um programa que pergunte em qual direção o usuário deseja contar (para cima [ c/C] ou para baixo [a/A]).
#Se ele selecionar para cima, peça o número superior e conte de 1 até esse número.
#Se ele selecionar para baixo, peça-lhe para inserir um número abaixo de 20 e, em seguida, faça uma contagem regressiva de 20 até esse número
#.Se ele inserir algo diferente de cima ou baixo, exiba a mensagem “Direção Invalida!".

dire = input("Contar para cima(C), ou para baixo (A) :").upper()

if dire == "C":
    for i in range(1, int(input("Digite um numero superior a 20 :")) + 1):
        print(i)
elif dire == "A":
    num = int(input("Digite um numero abaixo que 20:"))
    if num < 20:
        for i in range(20, num -1,-1):
            print(i)
    else:
        print("numero invalido!!")
else:
    print("Direçao invalida")

print("Programa finalizado.")
print("Ana Clara De Souza")