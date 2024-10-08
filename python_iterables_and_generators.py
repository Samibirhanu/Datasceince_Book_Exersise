# Create generators with function:
def generate_range(n):
    i = 0
    while i < n:
        yield i   # every call to yield produces a value of the genrator , its like return statment but a little differene
        i += 1

print(generate_range(5))

# loop that takes yielded values one at a time
for i in generate_range(10):
    print(f"i: {i}")

# create infinite sequance generator
def natural_numbers():
    """ returns 1, 2, 3, ...."""
    n = 1
    while True:
        yield n
        n += 1

evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)
print(evens_below_20)
# data processing pipelines 
# None of those computations *does* anything until we iterate 
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
evens_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in evens_squares if x % 10 == 6)
# and so on 

# python enumerate function  (value, index)

names = ["Alice", "Bob", "Charlie", "Debbie"]

# not pythonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# also not pythonic 
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1

# pythonic
for i, name in enumerate(names):
    print(f"name {i} is {name}")

