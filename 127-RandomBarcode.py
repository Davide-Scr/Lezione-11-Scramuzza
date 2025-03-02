import random

def genera_barcode(lanci):
    barcode = ""
    for _ in range(lanci):
        if random.randint(0, 1) == 0:
            barcode += "|"
        else:
            barcode += " "
    return barcode

# Numero di lanci della moneta
num_lanci = int(input("Inserisci il numero di lanci della moneta: "))

# Genera e stampa il codice a barre casuale
print(genera_barcode(num_lanci))
