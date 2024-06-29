from utils import numbers

num = int(input('Insert a value: '))
fact = numbers.factorial(num)
print(f'Number: {num}, Factorial: {fact}')
print(f'Number: {num}, Double: {numbers.double(num)}')
print(f'Number: {num}, Triple: {numbers.triple(num)}')