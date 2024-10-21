# Pyhotn is daynamically typed language
from typing import Union
from typing import List
def add(a, b):
    return a + b
assert add(10, 5) == 15,                   "+ is valid for numbers"
assert add([1, 2], [3]),                   "+ is valid for lists"
assert add("hi ", "there") == "hi there",  "+ is valid for strings" 

try:
    add(10, "five")
except TypeError:
    print("cannot add an int to a string")

# our program statically typed language
def add(a: int, b: int) -> int:
    return a + b
add(10, 5)                    # you'd like this to be ok
add("hi ", "there")           # you'd like this to be not ok

def secretly_ugly_function(value, opreation): ...
def ugly_function(value: int, opreation: Union[str, int, float, bool]) ->int:
    ...

def f(xs: List[int]) -> None:
    xs.append(1)

# This is how to type-annotate variables when you define them.
x: int = 5
values = []
best_so_far = None      # what is my type

# applie inline hints
from typing import Optional

values2: List[int] = []
best_so_far_so_good: Optional[float] = None        # allowed to be either a float or none

from typing import Dict, Iterable, Tuple

# key are string values are ints
counts: Dict[str, int] = {'data': 1, 'science': 2}

from typing import Callable

# the type hint says that repeater is a fucntion that takes 
# two arguments, a string and an int, and returns a string
def twice(repeater: Callable[[str, int],str], s:str) -> str:
    return repeater(s, 2)
def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)
assert twice(comma_repeater, "type hints") == "type hints, type hints", "error"

