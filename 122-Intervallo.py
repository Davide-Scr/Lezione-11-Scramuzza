a = int(input("Inserisci il valore di a: "))
b = int(input("Inserisci il valore di b: "))
if b < a:
    print("Errore: b deve essere maggiore o uguale ad a.")
else:
    somma = sum(range(a, b+1))
    print(f"La somma dei numeri da {a} a {b} è: {somma}")
