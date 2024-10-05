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

# list slicing with i:j all elements from i (inclusive) to j (not inclusive):
frist_three = x[:3]                 # [-1, 1, 2]
print(frist_three)
three_to_end = x[3:]                # [3, 4, ..., 9]
print(three_to_end)
last_three = x[-3:]                 # [7, 8, 9]
print(last_three)
without_first_and_last = x[1:-1]    # [1, .... 8]
print(without_first_and_last)
copy_of_x = x[:]                    # [-1, 1, .... , 9]
print(copy_of_x)

# slice can take third argument
every_third = x[::3]                # [-1, 3, 6, 9]
print(every_third)
every_second = x[::2]               # [-1, 2, 4, 6, 8]
print(every_second)
five_to_three = x[5:2:-1]           # [5, 4, 3]
print(five_to_three)
# increase by one to the left
two_to_four = x[2:5:1]              # [2, 3, 4]
print(two_to_four)

# Python in operator for checking list membership
# it examine each elemets of the list one at a time. not recommended for long list
print(1 in [1, 2, 3])  # True
print(0 in [1, 2, 3])  # False

# list concatnation use .extend to add items

x = [1, 2, 3]
x.extend([4, 5, 6])   # x is now [1, 2, 3, 4, 6]
print(x)

# list addition for concatnation
x = [1, 2, 3]
y = x + [4, 5, 6]    # y is [1, 2, 3, 4, 5, 6]
print(y)

# more frequently will append to lists one at a time
x = [1, 2, 3]
x.append(0)          # x is now [1, 2, 3, 0]
print(x)
y = x[-1]            # equals 0
print(y)
z = len(x)           # equals 4

# convinent to unpack lists with variable with the same number of element on both side
x, y = [1, 2]        # now x is 1, y is 2
print(x, y)

# common idiom to use an uderscore (_) for a value you're going to throw away:
_, y = [1, 2]  # y == 2, didnt care about the first element
print(y, _)