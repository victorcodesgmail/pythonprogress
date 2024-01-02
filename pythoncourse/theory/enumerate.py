fruits = ['apple', 'banana', 'cherry']

# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Value: {fruit}")



number_fruits = [fruits for index, fruit in enumerate(fruits)]
print(f"{number_fruits}")


    
    

# In this example, enumerate(fruits) generates pairs of index and value for
# each element in the fruits list. The loop then iterates over these pairs, 
# and in each iteration, index takes the value of the current index, and fruit 
# takes the value of the corresponding element.

# enumerate() is particularly useful when you need both 
# the index and the value of elements in a sequence during iteration.
# It simplifies the code compared to using a counter variable and indexing the iterable manually.