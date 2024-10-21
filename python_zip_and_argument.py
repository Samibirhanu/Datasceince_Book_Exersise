# zip two or more iterables togather:
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

print([pair for pair in zip(list1, list2)])     # is [('a', 1),('b', 2),('c', 3)]

# unzip a list using strange trick:
pairs = [('a', 1), ('b', 2),('c', 3)]
letters, numbers = zip(*pairs)
print(letters, numbers)

# asterisk (*) performs argument unpacking the same result to the previous one
letters, numbers = zip(('a', 1), ('b', 2),('c', 3))
print(letters, numbers)

# argument unpacking using function:
def add(a, b): return a + b
add(1,2)        # returns 3
try:
    add([1, 2])
except TypeError:
    print("add expects two inputs")   
print(add(*[1, 2]))                          # returns 3

