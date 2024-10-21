# tuples are lists immutable cousins. specify tuples by using parentesis
my_list = [1, 2]
print(my_list)
my_tuple = (1, 2)
other_tuple = 3, 2   # we can define without parentesis
print(other_tuple)
print(my_tuple)
my_list[1] = 3      # my_list is  now [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")

# convinent way to return multiple values from function
def sum_and_product(x, y):
    return (x + y), (x * y)   # those are returned as tuples (a pair of valurs)
sp = sum_and_product(2, 3)      # sp is (5, 6)
print(sp)
s, p = sum_and_product(5, 10)   # s is 15, p is 50
print(s, p)

# tuples and Lists used for multiple assignment
x, y = 1, 2   # now x is 1, y is 2
print(x, y)
x, y = y, x  # Pythonic way to swap variables; now x is 2, y is 1
print(x, y)

# NOT THIS WAY 
x, y = 2, 3
print(x, y)
x = y
y = x
print(x, y)   # now x and y is 3
