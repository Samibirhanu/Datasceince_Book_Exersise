# trnsforming list to another list
# [expression for item in iterable if condition]
even_numbers = [x for x in range(5) if x % 2 == 0]      # [0, 2, 4]
print(even_numbers)
squares = [x * x for x in range(5)]                     # [0, 1, 4, 9, 16]
print(squares)
even_squares = [x * x for x in even_numbers]            # [0, 4, 16]
print(even_squares)

even_numbers2 = []                 # create empty list
for x in range(5):                 # 0-5 
    if x % 2 == 0:                 # checking x divided by 2 is 0
        even_numbers2.append(x)    # add to the list
print(even_numbers2)

# dictionary
square_dict = {x: x * x for x in range(5)}      # {0: 0, 1: 1 ... 4: 16}
square_set = {x * x for x in [1, -1]}           # {1}

zeros = [0 for _ in even_numbers]               # has the same length as even_numbers     
print(zeros)

# using multiple fors
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]        # 100 pair (0, 0), (0, 1) .... (9, 9)
print(pairs)

