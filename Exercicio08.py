#EXE 008 - Defina uma variável chamada total como 0 (Zero).
#Peça ao usuário para inserir cinco números e, após cada entrada, pergunte se ele deseja que esse número seja incluído (S ou s, N ou n).
#Se ele desejar, adicione o número ao total. Se ele não quiser incluí-lo, não o adicione ao total. Depois de inserir todos os cinco números, exiba o total.
total = 0

for i in range(5):
    numero = int(input("digite o {}° numero:".format(i + 1)))
    incluir = input("Deseja incluir esse numero? (S/N)").upper()
    
    if incluir == "S":
        total += numero

    print("o total foi: ",total)
print("Programa finalizado.")
print("Ana Clara De Souza")