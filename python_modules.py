# Import module for including external downloaded libraries:
import re
my_regex = re.compile("0-9", re.I)

# If you already have re in your code use alias:
import re as regex
my_regex = regex.compile("0-9", re.I)

# Use this if module name is long or unwieldly name
import matplotlib.pyplot as plt 
plt.plot(...)

# For specific values from a module
from collections import defaultdict, Conter
lookup = defaultdict(int)
my_conter = Conter()

# Dont import unnesseserly values from module 
# which might inadvertently overwrite variables you've already defined:
