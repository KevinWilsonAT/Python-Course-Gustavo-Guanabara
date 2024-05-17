def counter(start, end, step):
    """
    -> Make a count and displays it

    :param start: counting start
    :param end: counting end
    :param step: counting step
    :return: no return
    """
    
    count = start
    while count <= end:
        print(f'{count}', end='... ')
        count+= step
    print('END COUNTING')

help(counter)
counter(2, 10, 2)