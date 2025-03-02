base = int(input("Inserisci la base: "))
esponente = int(input("Inserisci l'esponente massimo: "))
for i in range(esponente+1):
    print(f"{base}^{i} = {base**i}")
