def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return 2 * f(x)
    
    # And  return that new function
    return g
a = doubler(4)
print(a)