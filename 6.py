def sumsquare(num):
    return num*(2*num + 1)*(num+1)/6

def squaresum(num):
    return (num*(num+1)/2)**2

print(squaresum(100)-sumsquare(100))
