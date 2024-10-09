# zip will compress two or more iterables togather
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

[pair for pair in zip(list1, list2)]    # is [('a', 1),('b', 2), ('c', 3)]

# unzip the list using 
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(letters)
print(numbers)

letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))

def add(a, b): return a + b
add(1, 2)       # returns 3
try:
    add[1, 2]
except TypeError:
    print("add expects two inputs")

add(*[1, 2]) # returns 3
