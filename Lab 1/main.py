from math import floor


def tenth_to_rth(num, r):
    if num == 0:
        return ""
    return tenth_to_rth(num // r, r) + str(num % r)

def tenth_to_rth_fractional(num, r):
    if floor(num * r) == 1:
        return "1"
    return str(floor(num * r)) + tenth_to_rth_fractional(num - floor(num), r)

def rth_to_tenth(num, r, length):
    if length == 0:
        return num
    return num // 10 ** (length - 1) * r ** (length - 1) + rth_to_tenth(num % 10 ** (length - 1), r, length - 1)

def solve(num, r):
    pass



print(tenth_to_rth_fractional(0.14, 2))
