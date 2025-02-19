#EXE 005 - Peça ao usuário para inserir um número que deseja a tabuada e, em seguida, exibir a tabuada para esse número.
numero = int(input("Digite um numero da tabuada: "))

for i in range(1 , 11):
    print("{} x {} = {}".format(numero,i,numero * i))
print("Programa finalizado.")
print("Ana Clara De Souza")