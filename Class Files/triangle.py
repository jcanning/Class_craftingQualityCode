def area(base, height):
    return base * height / 2

def perimeter (side1, side2, side3):
    return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
    '''(number, number, number) -> float

    return the semiperimeter of a triangle with sites of
    length side1, side2, and side3.
    
    >>> semiperimeter(3, 4, 5)
    6.0
    >>> semiperimeter(10.5, 6, 9.3)
    12.9
    '''
    return perimeter(side1,side2,side3) / 2
