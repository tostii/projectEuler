from functools import reduce

def gcd(x, y):
    while y:
        tempx = x
        x = y
        y = tempx % y
    return x

def lcm(x,y):
    return (x*y)/gcd(x,y)


print(reduce(lcm,range(1,20)))


