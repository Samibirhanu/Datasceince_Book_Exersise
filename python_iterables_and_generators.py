# create generators with yield operator
def generator_range(n):
    i = 0
    while i < n:
        yield i         # every call to yield produces a value of the generator
        i += 1
# for loop to consume yielded values
for i in generator_range(10):
    print(f"i: {i}")

def natural_number():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1
    
evens_below_20 = (i for i in generator_range(20) if i % 2 == 0)

# none of these computations *does* anything until we iterate
data = natural_number()
evens = (x for x in data if x % 2 ==2)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)

# enumerate function, turns values into pairs(index, value)
names = ["Alice", "Bob", "Chalie", "Debbie"]

# not pytonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# also not pythonic
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1

# pythonic way
for i, name in enumerate(names):
    print(f"name {i} is {name}")


