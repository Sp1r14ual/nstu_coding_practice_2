def tenth_to_rth(num, r):
    if num == 0:
        return ""
    return tenth_to_rth(num // r, r) + str(num % r)

def rth_to_tenth(num, r, length):
    if length == 0:
        return num
    return num // 10 ** (length - 1) * r ** (length - 1) + rth_to_tenth(num % 10 ** (length - 1), r, length - 1)



print(rth_to_tenth(101010, 8, 6))
