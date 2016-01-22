def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def count():
    iterate = 0
    sequence = 0
    while fib(iterate) < 4000000:
        if fib(iterate) % 2 == 0:
            sequence += fib(iterate)
        iterate+=1
    return sequence

print(count())
