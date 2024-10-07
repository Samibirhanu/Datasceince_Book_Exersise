# set is another useful data structure. it is a collection of dictnict elements. defind with curly braces
primes_below_10 = {2, 3, 5, 7}
print(primes_below_10)
# does'nt work for empty sets as {} already means "empty dict". in that case you will need to use set() itself:

s = set()       # empty set
print(s)        
s.add(1)        # s is now {1}
print(s)
s.add(2)        # s is now {1, 2}
print(s)
s.add(2)        # s is still {1, 2}
print(s)

x=len(s)
y = 2 in s       # equals True its fast operation
print(y)

# main use of set - very fast on "in" operation, if we have large collection of items and use membership test set is more appropriate than a list.
stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list             # False but have to check every element
stopwords_set = set(stopwords_list)
"zip" in stopwords_list             # very fast to check

# find dictnict items in a collection
item_list = [1, 2, 3, 1, 2 ,3]
num_items = len(item_list)           # 6
item_set = set(item_list)            # {1, 2, 3}
print(item_set)
num_distinict_items = len(item_set)  # 3
distinict_item_list = list(item_set) # [1, 2, 3]

# we use set less frequantly than dictionary and list

