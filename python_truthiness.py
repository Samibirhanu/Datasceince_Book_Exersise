# Booleans in python wor as in most other languages except they are capitalized
one_is_less_than_two = 1 < 2    # equals True
print(one_is_less_than_two)
true_equals_false = True == False # equals False
print(true_equals_false)

# none value
x = None
assert x == None, "this is the not the pytonic way to check for none"
assert x is None, "this is the pythonic way to check for None"

# the following are  falsy in python

# False
# None
# []
# {}
# set()
# 0
# 0.0

# s = some_function_that_returns_a_string()
# if s:
#     first_char = s[0]
# else:
#     first_char = ""
# s = {}
# if s:
#     print("s is true")
# else:
#     print(f"{s} s is false")
# first_char = s and s[0]
# print(first_char)

safe_x = x or 0
print(safe_x)
safe_x = x if x is not None else 0
print(safe_x)

# all function
all([True, 1, {3}])     # True, all are truthy
all([True, 1, {}])      # False, {} is truthy
any([True, 1, {}])      # True, True is truthy
all([])                 # True, no falsy elements in the list
any([])                 # False, no truthy element in the list

