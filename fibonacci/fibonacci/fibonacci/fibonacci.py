def fib_iteration(number):
    a, b = 0, 1
    for x in range(number):
        a, b = b, a+b
    return a

def fib_recursive(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        return fib_recursive(number-1) + fib_recursive(number-2)

print(fib_iteration(10))
print(fib_recursive(10))