def function_runner(f):
    """ (function) -> NoneType

    Call F.
    """

    f()

def function_1():
    """ () -> NoneType

    Print that this function was called.
    """

    print('function_1 was called.')

def function_2():
    """ () -> NoneType

    Print that this function was called.
    """

    print('function_2 was called.')


if __name__ == '__main__':
    function_runner(function_1)

