def ranks(*n, status=False):

    """
    -> Function that analyzes the ranks e status from many students.
    :param n: one or more students' ranks (allow multiple rank entries).
    :param status: optional value, indicating if should or not add the status.
    :return: dictionary with various informations about the class status.
    """

    r=dict()
    r['total'] = len(n)
    r['greater'] = max(n)
    r['lesser'] = min(n)
    r['average'] = sum(n) / len (n)
    if status:
        if r['average'] >= 7:
            r['status'] = 'GOOD'
        elif r['average'] >= 5:
            r['status'] = 'AVERAGE'
        else:
            r['status'] = 'POOR'
    return r


# Main Program
response = ranks(5.5, 2.5, 1.5, status=True)
print(response)
help(ranks)