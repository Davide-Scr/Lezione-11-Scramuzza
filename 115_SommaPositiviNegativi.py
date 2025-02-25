N = int(input("Quanti numeri vuoi inserire? "))
positivi = 0
negativi = 0
for _ in range(N):
    num = int(input("Inserisci un numero: "))
    if num > 0:
        positivi += num
    elif num < 0:
        negativi += num
print(f"Somma dei positivi: {positivi}")
print(f"Somma dei negativi: {negativi}")
