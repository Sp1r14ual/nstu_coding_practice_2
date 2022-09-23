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

def rth_to_tenth_fractional(num, r, length):
    if length == -1:
        return num * r ** (length)
    return num % 10 * r ** (length + 1) + rth_to_tenth_fractional(num // 10, r, length + 1)

def solve(num, r):
    whole = floor(num)
    whole_length = len(str(whole))
    fraction = int(str(num)[str(num).index(".") + 1 : ])
    fraction_length = len(str(fraction)) + 1
    return rth_to_tenth(whole, r, whole_length) + rth_to_tenth_fractional(fraction, r, -fraction_length)

print(solve(101.11, 2))
