numero = int(input("Inserisci un numero: "))
primo = True
if numero < 2:
    primo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break
if primo:
  print(f"{numero} è un numero primo.")
else:
    print(f"{numero} non è un numero primo.")
