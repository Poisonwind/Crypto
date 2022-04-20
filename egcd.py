
def egcd(a, b):
    # return gcd, x, y
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

'''
Using the two primes p = 26513, q = 32321, find the integers u,v such that

p * u + q * v = gcd(p,q)

Enter whichever of u and v is the lower number as the flag.

'''

def gcdmod(a, b):

    q_arr = []

    while b != 0:
        if a > b:
            r = a%b
            q = a//b
            q_arr.append(a//b)
            a,b = b,r
        elif b > a:
            a,b = b,a
    return q_arr[:-1]

def find_numbers(val0, val1, q_arr):


    '''
    x[0] = 1 ; x[1] = 0
    y[0] = 0 ; y[1] = 1

    x[i] = x[i-2]-q[i]*x[i-1]
    '''

    i = 2
    val_arr = []
    val_arr.append(val0)
    val_arr.append(val1)

    for q in q_arr:
        val_arr.append(0)
        val_arr[i] = val_arr[i-2] - q*val_arr[i-1]
        i += 1

    return val_arr

def min(a, b):
    if a < b:
        return a
    else:
        return b

num1 = 26513
num2 = 32321

if __name__ == '__main__':
    
    q_arr = gcdmod(num1, num2)
    #print(q_arr)

    x_arr = find_numbers(1, 0, q_arr)
    #print(x_arr)
    y_arr = find_numbers(0, 1, q_arr)
    #print(y_arr)

    print(min(x_arr[-1], y_arr[-1]))

    