

def gcd(a, b):
    while a != b:
        if a > b:
            a -=b
        elif b > a:
            b -=a

    return a


print(gcd(66528, 52920))

    