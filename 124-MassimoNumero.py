N = int(input("Quanti numeri vuoi inserire? "))
max_num = float('-inf')
for _ in range(N):
    num = int(input("Inserisci un numero: "))
    if num > max_num:
        max_num = num
print(f"Il numero massimo è: {max_num}")
