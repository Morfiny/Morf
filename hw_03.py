 #Вопрос 1

def g(n):
    if n <= 3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    if n <= 3:
        return n
    else:
        a, b, c = 1, 2, 3
        for i in range(4, n+1):
            a, b, c = b, c, c + 2*b + 3*a
        return c

 #Вопрос 2

def has_seven(k):
    return '7' in str(k)

 #Вопрос 3

def pingpong(n):
    def helper(index, value, direction):
        if index == n:
            return value
        elif index % 7 == 0 or has_seven(index):
            return helper(index + 1, value - direction, -direction)
        else:
            return helper(index + 1, value + direction, direction)

    return helper(1, 1, 1)

 #Вопрос 4

def ten_pairs(n):
    if n < 10:
        return 0

    last_digit = n % 10
    remaining_digits = n // 10

    count = count_pairs(last_digit, remaining_digits) + ten_pairs(remaining_digits)

    return count

def count_pairs(last_digit, n):
    if n == 0:
        return 0

    current_digit = n % 10
    remaining_digits = n // 10

    if current_digit + last_digit == 10:
        return 1 + count_pairs(last_digit, remaining_digits)
    else:
        return count_pairs(last_digit, remaining_digits)

 #Вопрос 5

def count_change(amount):
    return count_partitions(amount, 1)

def count_partitions(amount, smallest_coin):
 if amount == 0:
     return 1
 elif amount < 0:
     return 0
 else:
     count = 0
     coin = smallest_coin
     while coin <= amount:
         count += count_partitions(amount - coin, coin)
         coin *= 2
     return count