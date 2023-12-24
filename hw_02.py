
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
    return lambda x: f(x)

def two(f):
    return lambda x: f(f(x))


def church_to_int(n):
    return n(lambda x: x + 1)(0)

def add_church(m, n):
    return lambda f: lambda x: m(f)(n(f)(x))

def mul_church(m, n):
    return lambda f: m(n(f))
def pow_church(m, n):
    return n(m)