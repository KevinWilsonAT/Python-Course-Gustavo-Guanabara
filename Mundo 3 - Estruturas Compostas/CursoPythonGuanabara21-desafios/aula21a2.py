def sum(a=0, b=0, c=0): # adding '= 0' to the parameters makes them optional parameters
    """
    -> Sum 3 numbers and display the result

    :param a: the first value
    :param b: the second value
    :param c: the third value
    :return: no return
    """
    
    s = a+b+c

    print(f'{a} + {b} + {c} = {s}')

sum(3, 2, 5)
sum(8, 4)
sum(5)
sum()