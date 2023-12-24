
# Вопрос 1.
def product(n, term):
    result = 1
    for i in range(1, n + 1):
        result *= term(i)
    return result


def factorial(n):
    if (n >= 0):
        return product(n, lambda x: x)
    return 0


# Вопрос 2.

def accumulate(combiner, base, n, term):
    result = base
    for i in range(1, n + 1):
        result = combiner(result, term(i))
    return result


def summation_using_accumulate(n, term):
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    return accumulate(mul, 1, n, term)


# Вопрос 3.

def double(f):
    def double_f(x):
        return f(f(x))
    return double_f

# Вопрос 4.

def make_repeater(f, n):
    def repeater(x):
        result = x
        for _ in range(n):
            result = f(result)
        return result
    return repeater


def make_repeater(f, n):
    return accumulate(compose1, [f] * n, identity)


# Вопрос 5.

def one(f):
    """Число Чёрча 1."""
    return lambda x: f(x)

def two(f):
    """Число Чёрча 2."""
    return lambda x: f(f(x))

three = successor(two)

def church_to_int(n):
    """Преобразует число Чёрча n в целое число Python.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    return n(lambda x: x + 1)(0)

def add_church(m, n):
    """Возвращает число Чёрча m + n для чисел Чёрча m и n.

    >>> church_to_int(add_church(two, three))
    5
    """
    return lambda f: lambda x: m(f)(n(f)(x))

def mul_church(m, n):
    """Возвращает число Чёрча m * n для чисел Чёрча m и n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    return lambda f: m(n(f))

def pow_church(m, n):
    """Возвращает число Чёрча m ** n для чисел Чёрча m и n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    return n(m)