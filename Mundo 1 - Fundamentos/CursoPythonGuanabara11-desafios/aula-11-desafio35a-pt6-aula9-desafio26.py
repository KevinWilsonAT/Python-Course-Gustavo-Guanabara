colors = {
    'clean': '\033[m',
    'let_oc': '\033[0;32m',
    '1st_oc': '\033[0;31m',
    'last_oc': '\033[0;36m'
}

text = str(input("Insert a text: ")).upper().strip()

print('The letter "A" appears {}{}{} times'
      .format(colors['let_oc'], text.count('A'), colors['clean']))
print('The first letter "A" appears in the position {}{}{}'
      .format(colors['1st_oc'], text.find("A")+1, colors['clean']))
print('The last letter "A" appears in the position {}{}{}'
      .format(colors['last_oc'], text.rfind("A")+1, colors['clean']))
