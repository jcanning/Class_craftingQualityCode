def linear_search(L, v):
    """ (list, object) -> int

    Return the index of hte first occurrence of v in L, or
    return -1 if v is not in L.

    >>> linear_search([2,3,5,3], 2)
    0
    >>> linear_search([2,3,5,3],5)
    2
    >>> linear_search([2,3,5,3],8)
    -1
    """

    i = 0

    length = len(L)

    while i != length and v != L[i]:
        i = i + 1

    if i == length:
        return -1
    else:
        return i


def binary_search(L, v):
    """ (list, object) -> int

    Return the index of the first occurrence of v in L, or
    return -1 if v is not in L.

    >>> binary_search([2, 3, 5, 7], 2)
    0
    >>> binary_search([2, 3, 5 ,5], 5)
    2
    >>> binary_search([2, 3, 5, 7],8)
    -1
    """

    b = 0
    e = len(L) -1

    while b <= e:
        m = (b + e) //2
        if L[m] < v:
            b = m + 1
        else:
            e = m - 1
            
    if b == len(L) or L[b] != v:
        return - 1
    else:
        return b
