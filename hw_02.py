def square(x):
    """Возвращает квадрат x."""
    return x * x


# Вопрос 1.

def product(n, term):
    sum = 1
    for i in range(1, n + 1):
        sum *= term(i)
    return sum


def factorial(n):
    if (n >= 0):
        return product(n, lambda x: x)
    return 0


# Вопрос 2.

def accumulate(combiner, start, n, term):
    total = start
    for i in range(n):
        total = combiner(total, term(i + 1))
    return total


def summation_using_accumulate(n, term):
    return accumulate(lambda x, y: x + y, 0, n, term)


def product_using_accumulate(n, term):
    return accumulate(lambda x, y: x * y, 1, n, term)


# Вопрос 3.

def double(f):
    return lambda x: f(f(x))


# Вопрос 4.

def repeated(f, n):
    return f if n == 1 else lambda x: f(repeated(f, n - 1)(x))


def compose1(f, g):
    def h(x):
        return f(g(x))

    return h


# Вопрос 5.

def zero(f):
    return lambda x: x


def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    return lambda x: f(x)


def two(f):
    return lambda x: f(f(x))


def three(f):
    return lambda x: f(f(f(x)))


def four(f):
    return lambda x: f(f(f(f(x))))


def church_to_int(n):
    return n(lambda x: x + 1)(0)


def add_church(m, n):
    return lambda f: lambda x: m(f)(n(f)(x))


def mul_church(m, n):
    return lambda x: m(n(x))