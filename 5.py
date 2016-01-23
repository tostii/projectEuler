from functools import reduce

def lcm(x,y):
    return (x*y)/gcd(x,y)

def gcd(x, y):
    while y:
        tempx = x
        x = y
        y = tempx % y
    return x



print(reduce(lcm,range(1,20)))


