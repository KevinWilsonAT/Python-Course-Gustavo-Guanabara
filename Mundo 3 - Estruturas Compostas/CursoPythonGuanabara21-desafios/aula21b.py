def sum(a=0, b=0, c=0): # adding '= 0' to the parameters makes them optional parameters
    """
    -> Sum 3 numbers and display the result

    :param a: the first value
    :param b: the second value
    :param c: the third value
    """

    s = a+b+c
    return s

r1 = sum(3, 2, 5)
r2 = sum(1, 7)
r3 = sum(4)

print(f'The results of the sums are: {r1}, {r2} and {r3}')