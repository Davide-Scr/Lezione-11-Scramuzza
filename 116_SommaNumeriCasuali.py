import random
N = int(input("Quanti numeri casuali vuoi generare? "))
somma = 0
for _ in range(N):
    num = random.randint(0, 100)
    print(f"Numero generato: {num}")
    somma += num
print(f"La somma dei numeri generati è: {somma}")
