import re 

re_examples = [
    not re.match("a", "cat"),       # 'cat' does'nt start with 'a'
    re.search("a", "cat"),          # 'cat' has an 'a' in it
    not re.search("c", "dog"),      # 'dog' doesn't have a 'c' in it.
    3 == len(re.split("[ab]", "carbs")), # split on a or b to ['c', 'r', 's']
    "R-D-" == re.sub("[0-9]", "-", "R2D2") # replace digits with dashes
]

assert all(re_examples), "all the regex examples should be True"