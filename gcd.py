'''
Now calculate gcd(a,b) for a = 66528, b = 52920

'''

def gcd(a, b):
    while a != b:
        if a > b:
            a -=b
        elif b > a:
            b -=a

    return a

def gcdmod(a, b):
    while b != 0:
        if a > b:
            c = a%b
            a,b = b,c
        elif b > a:
            a,b = b,a
    return a


print(gcd(66528, 52920))

#################################################