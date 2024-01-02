import functools

letters = ["H","E", "L", "L","O",]

word = lambda x , y: x+y

reducedword = functools.reduce(word, letters)

print(reducedword)

#reduce(function, iterable)