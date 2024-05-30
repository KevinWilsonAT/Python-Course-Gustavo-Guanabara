def factorial(n, show = False):
    """
    -> Calculates the factorial of a number.
    :param n: The number to be calculated
    :param show: (Optional) Display / Hide the calculation
    :return: The factorial value of the number n
    """

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

n = int(input("Insert the number to calculate its factorial: "))
option = str(input("Show the factorial calculation? (Y/N) ").strip().upper()[0])
if option in "Yy":
    show = True
else:
    show =False

print(factorial(n, show))