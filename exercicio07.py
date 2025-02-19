#EXE 007 . Peça ao usuário para inserir seu nome e um número. Se o número for menor que 10, 
#exiba o nome dele esse número de vezes; caso contrário, exiba a mensagem “Numero muito alto" três vezes.

nome = input("Digite seu nome: ")
num = int(input("Digite um numero: "))
if num  < 10:
    for i in range(num):
        print(nome)
else:
    print("numero muito alto")