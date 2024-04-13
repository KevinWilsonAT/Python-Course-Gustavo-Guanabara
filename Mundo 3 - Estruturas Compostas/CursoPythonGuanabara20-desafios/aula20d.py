def sum(* values):
    s = 0
    for num in values:
        s += num
    print(f'Values summed: {values}, total: {s}')


sum(5, 2)

sum(2, 9, 4)