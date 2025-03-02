num = int(input("Inserisci il numero: "))
massimo = int(input("Inserisci il valore massimo: "))
for i in range(massimo, 0, -1):
    if i % num == 0:
        print(i, end=" ")
