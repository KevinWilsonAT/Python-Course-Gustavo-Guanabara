name = 'Kevin'
age = 29
salary = 1000.00

# PYTHON 3.6+
print(f"{name} is {age} years old.")
print(f"{name} is {age} years old and has a salary of R${salary}.")

# PYTHON 3
print("{} is {} years old.".format(name, age))
print("{} is {} years old and has a salary of R${}.".format(name, age, salary))
# PYTHON 2
print("%s is %d years old." % (name, age))
print("%s is %d years old and has a salary of R$%.1f." % (name, age, salary))
