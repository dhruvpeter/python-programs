def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1)+fib(n-2)


n = int(input("No. of terms: "))
i = 1
while(i <= n):
    print(fib(i))
    i += 1
