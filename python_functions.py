# I python functions are defined using def
def double(x):
    """ This is docstring which is other type of comment specifically this one 
    will use for explaining the what the function does. """

    return x * 2

print(double(20)) # 40

# Python functions are first-class. so that we can assign them to variables and pass them into functions like any argument
def apply_to_one(f):
    """ Calls the function f with 10 as its argument"""
    return f(10)
my_double = double # refers to the previosly defined function
print(my_double) 
x = apply_to_one(my_double) # equals 20
print(x)

# Short anonymous function, or lambdas:
y = apply_to_one(lambda x: x+4) # equals 14
print(y)

# Assign lambdas to variables. 
another_double = lambda x: 2* x  # Its not suggested 
# This is suggested one
def another_double(x):
    """The function return x multiplied by 2 """
    return 2 * x

# You can give default argument for function
def my_print(message = "my default message"):
    print(message)

my_print("Hello") # prints 'hello'
my_print()        # prints 'my default message'

# Sometimes useful to specify argments by name:
def full_name(first = "what's-his-name", last = "Something"):
    return first + " " + last

print(full_name("Samuel", "Birhanu")) # prints 'samuel Birhanu'
print(full_name("Samuel"))            # prints 'Samuel Something
print(full_name(last = "Birhanu"))           # prints 'what's-his-name Birhanu'


