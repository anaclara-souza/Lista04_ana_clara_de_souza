#EXE 010 - Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
#Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa".
# Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".
quant = int(input("Quantas pessoas ira convidar?  "))

if quant < 10:
    for i in range(quant):
        nome = input("Digite o nome do convidado: ")
        print(nome,"esta convidado para a festa!! ")
else:
    print("Tem muitos convidados!! ")

print("Programa finalizado.")
print("Ana Clara De Souza")