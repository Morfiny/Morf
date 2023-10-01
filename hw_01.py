from operator import add, sub
def a_plus_abs_b(a, b):
    """Возвращает a+abs(b), но не использует abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        op = sub (a, b)
    else:
        op = add (a, b)
    return op