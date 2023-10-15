# Вопрос 4
def both_pozitive(x, y):
    if (x > 0 and y > 0):
        return True
    else:
        return False

# Вопрос 5

def sum_digits(n):
    number = 456729634
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10



# Вопрос 8
def falling(n, k):
    a = 1
    while k > 0:
        k = k - 1
        a = a * n
        n = n - 1
    return a



# Вопрос 9
def double_eights(n):
    while n > 0:
        a = n % 10
        n = n // 10
        b = n % 10
        if a == 8 and b == 8:
            return True
    return False