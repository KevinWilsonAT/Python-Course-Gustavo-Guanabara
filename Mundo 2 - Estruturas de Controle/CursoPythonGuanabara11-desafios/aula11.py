# print('\033[style;text;backgroundm text goes here)

# style: 0 (no style), 1 (bold), 4 (underline) 7(negative)
# text (colors): 30 (black), 31 (red), 32 (green), 33 (yellow),
# 34 (blue), 35 (purple), 36 (), 37 ()
# background (colors): 40 (black), 41 (red), 42 (green), 43 (yellow),
# 44 (blue), 45 (purple), 46 (), 47 ()

print('\033[0;30;41mTeste') # no style, black text, red background
print('\033[4;33;44mTeste') # underline style, yellow text, blue background
print('\033[1;35;43mTeste') # bold style, purple text, blue background
print('\033[0;42mTeste') # no style, default text, green background
print('\033[0;40mTeste') # no style, default text, black background
print('\033[7mTeste') # inverted text/background colors

