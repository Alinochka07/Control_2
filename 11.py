def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur

for i in fibonacci():
    print(i)
    if i > 100:
        break


fib = fibonacci()
print(next(fib))

print(next(fib))


for num, fib in enumerate(fibonacci()):
    print('{0}: {1}'.format(num, fib))
    if num > 9:
        break