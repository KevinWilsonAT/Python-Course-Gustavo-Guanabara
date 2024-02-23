count = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen',
         'Twenty')

while True:
    number = int(input('Type a number between 0 and 20: '))
    if 0 <= number <= 20:
        break
    print('Try again! ', end='')
print(f'The number {number} is written {count[number]}')
