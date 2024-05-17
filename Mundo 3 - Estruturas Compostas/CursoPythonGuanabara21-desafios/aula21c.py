def factorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


f1 = factorial(5)
f2 = factorial(4)
f3 = factorial()

print(f'The results of the factorials are: {f1}, {f2} and {f3}')