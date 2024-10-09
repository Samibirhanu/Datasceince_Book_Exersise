# provide a way of searching text
import re
re_examples = [                     # all of those are True, because
    not re.match("a", "cat"),        # 'car' doesnt start with 'a'
    re.search("t", "cat"),           # 'cat' has an 'a' in it
    not re.search("c", "dog"),       # 'dog' doesn't have 'c' in it.
    3 == len(re.split("[ab]", "carbs")) # split on a or b to ['c', 'r', 's']
]   
assert all(re_examples), "all the regex examples should be True"
