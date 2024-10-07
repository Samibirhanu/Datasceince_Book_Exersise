# Define class using class keyword and a PascalCase name
class CountingClicker:
    """ A class can/should have a docstring, just like a function"""
    def __init__(self, count = 0):
        self.count = count
    def __repr__(self):
        return f"CountingClicker(count={self.count})"
    def click(self, num_times = 1):
        """click the clicker some number of times."""
        self.count += num_times
    def read(self):
        return self.count
    def reset(self):
        self.count = 0
    
# clicker1 = CountingClicker()            # initialized to 0
# clicker2 = CountingClicker(100)         # starts with count=100
# clicker3 = CountingClicker(count = 100) # more explicit way of doing the same
# print(clicker1)
# print(clicker2)
# print(clicker3)

# Use assert to test
clicker = CountingClicker()         # object created
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset clicker should be back to 0"

# A subclass ingerits all the behavior of its parent class
class NoResetClicker(CountingClicker):
    # this class has all the same methods as CountingClicker

    # lets modify reset method
    def reset(self):
        pass

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"

