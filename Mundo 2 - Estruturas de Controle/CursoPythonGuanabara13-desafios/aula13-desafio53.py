text = str(input('Insert a text: ')).strip().upper()
words = text.split()
combined = ''.join(words)
reverse = combined[::-1]

print('The reverse of {} is {}'.format(combined, reverse))
if reverse == combined:
    print('We have a palindrome')
else:
    print('The inserted text is not a palindrome')
    