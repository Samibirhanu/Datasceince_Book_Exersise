def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return 2 * f(x)
    
    # And return that new function
    return g

def f1(x):
    return x +1
g= doubler(f1)
assert g(3) == 8, "(3 + 1) * should equal 8"
assert g(-1) ==0, "(-1 + 1) * should equal 0"

# doesnt work with functions that take more than a single argumnet
def f2(x, y):
    return x + y

g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("as defined, g only takes one argument")

def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)

magic(1, 2, key="word", key2="word2")

#prints 
# unnamed args: (1, 2)
# keyword args: {'key': 'word', 'key': 'word2'}

# for list tuple
def other_way_magic(x, y, z):
    return x + y + z
x_y_list =[1, 2]
z_dict = {"z": 3}
assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should be 6"

# produce higher-order functions whose inputs can accept arbitrary arguments:
def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """"whatever arguments g is supplied, pass them throgh to f"""
        return 2 * f(*args, **kwargs)
    return g
g = doubler_correct(f2)
assert g(1, 2) == 6, "doubler should work now"
