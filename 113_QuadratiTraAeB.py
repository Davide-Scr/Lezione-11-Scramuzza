A = int(input("Inserisci il primo numero: "))
B = int(input("Inserisci il secondo numero: "))
if A > B:
    A, B = B, A
for i in range(A, B+1):
    print(f"{i}^2 = {i**2}")
