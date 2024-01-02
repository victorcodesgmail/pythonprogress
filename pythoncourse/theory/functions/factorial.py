import functools

num = [5,4,3,2,1]

#reduce(function, iterable)

fact = lambda x, y: x*y

factorial = functools.reduce(fact, num)

print(factorial)