def isPrime(num):
    max = int(num ** 0.5)
    for x in range(2,max + 1):
        if num % x == 0:
            return False
    return True

myPrime = 0
currNum = 2

while myPrime != 10001:
    if isPrime(currNum):
        print(currNum)
        myPrime = myPrime + 1
    currNum = currNum +1