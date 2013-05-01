def print_ints(n):
    """ (int) -> NoneType

    Print the intergers from 1 to n, inclusive.
    """

    for i in range(1, n + 1):
        print(i)

def print_odd_ints(n):
    """ (int) -> NoneType

    Print the odd integers from 1 to n, inclusive.
    """

    for i in range (1, n + 1, 2):
        print(i)

def print_pairs(n):
    """ (int) -> NoneType

    print all combinations of pairs of integers 1 to n,
    inclusive.
    """

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i, j)
            
def print_double_step(n):
    """ (int) -> NoneType

    Print integers from 1 to n inclusive, with an intial
    step size of 1 and each subsequent step size being
    twice as large as it was previously.
    """

    i = 1
    while i < n + 1:
        print(i)
        i = i * 2
