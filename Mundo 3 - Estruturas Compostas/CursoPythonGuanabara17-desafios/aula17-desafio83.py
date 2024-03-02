print("PROGRAM STARTED.")
print("="*50)

expression = str(input("Insert expression:"))
stack = list()
left_par = right_par = 0

for symbol in expression:
    if symbol == "(":
        stack.append("(")
        left_par += 1
    elif symbol == ")":
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(")")
            break
        right_par += 1

if len(stack) == 0:
    print("Your expression is valid.")
    print(f"Number of left parenthesis: {left_par}")
    print(f"Number of right parenthesis: {right_par}")
else:
    print("Your expression is not valid.")
    print(f"Number of left parenthesis: {left_par}")
    print(f"Number of right parenthesis: {right_par}")

print("="*50)
print("PROGRAM ENDED.")
