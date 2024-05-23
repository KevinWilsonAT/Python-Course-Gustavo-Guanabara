def vote(b_year):
    from datetime import date

    today = date.today().year
    age = today - b_year

    if age < 16:
        return f"With {age} years old, the voting is denied"

    elif 16 <= age < 18 or age > 65:
        return f"With {age} years old, the voting is optional"
    
    else:
        return f"With {age} years old, the voting is obligatory"
        

print("PROGRAM STARTED")

b_year = int(input("Enter your birth year:"))
print(vote(b_year))

print("PROGRAM ENDED")