#EXE 006 - Peça um número abaixo de 50 e, em seguida, faça uma contagem regressiva de 50 até esse número, certificando-se de mostrar o número que eles inseriram na saída.
numero = int(input("Digiteum numero abaixo de 50: "))

if numero >= 50:
    print("o numero deve ser menor que 50.")
else:
    for i in range(50,numero,-1,):
        print(i)
    print(numero)
print("Programa finalizado.")
print("Ana Clara De Souza")