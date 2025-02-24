N = int(input("Scrivi un numero:"))

mumeri_primi = []

for i in range(2, N + 1):
    is_prime = True
    for j in range (2, i):
        if i % j == 0:
            if is_prime == False
    if is_prime:
        numeri_primi.append(i)

print("I numeri primi fino a", N, "sono", numeri_primi)