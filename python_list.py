# Integer list
integer_list = [1, 2, 3]
print(integer_list)
unorders_list = [3,2,1]
print(unorders_list)
# Different data types in list
hetrogeneous_list = ["string", 0.1, True]
#list containing another list
list_of_lists = [integer_list, hetrogeneous_list, []]

# length of the list
list_length = len(integer_list) # equals 3
print(list_length)
list_sum = sum(integer_list)    # equals 6
print(list_sum)

# Accessing nth element of list with square brackets:
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0]   # equals 0, lists are 0-indexed
print(zero)   
one = x[1]    # equals 1
print(one)
nine = x[-1]  # equals 9, 'pythonic' for last element
print(nine)
eight = x[-2] # equals 8, 'pythonic' for next-to-last element
print(eight)
x[0] = -1     # [-1, 1, 2, ..., 9]
print(x)

