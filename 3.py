def largestPrime(n):
    i = 2
    while i ** 2 <= n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n

num = 600851475143
print(largestPrime(num))