sal = float(input("Employee's salary: R$"))
sal_augm = sal + (sal * 15/100)

print("The employee's salary was R${:.2f}; with a 15% increase: R${:.2f}".format(sal, sal_augm))
