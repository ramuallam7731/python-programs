n = int(input())
is_prime = True
for i in range(2, n):
    if (i % n) == 0:
        is_prime = False
        break
print(is_prime)
