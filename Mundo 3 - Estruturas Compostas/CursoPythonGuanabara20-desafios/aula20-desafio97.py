def write(msg):
    n = len(msg) + 4

    print(n)
    print('~' * n)
    print(f'  {msg}')
    print('~' * n)

 
print("PROGRAM STARTED.")
print("=" * 50)

write(str(input('Text: ')))

print("=" * 50)
print("PROGRAM ENDED.")
