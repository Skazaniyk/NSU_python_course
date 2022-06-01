def fib_recursion(n):
    if n <= 2:
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)


def fib_while(n):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a + b
    return b

n = int(input())
print(fib_while(n))
print(fib_recursion(n))
