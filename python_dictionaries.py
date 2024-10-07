# Faundamental data structure is dictinory. has values and keys and its mutable
empty_dict = {}                     # Pyhonic
empty_dict2 = dict()                # less Pythonic
grades = {"Joel": 80, "Tim": 95}    # dictionary literal
print(grades)

# look up the value with using key
joels_grade = grades["Joel"]        # equals 80
print(joels_grade)

# key error when you ask thats not in the dictionary
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

#check the existence of a key with "in"
joel_has_grade = "Joel" in grades  # True
print(joel_has_grade)
kate_has_grade = "Kate" in grades  # False
print(kate_has_grade)

# this membership check is fast in large dictionaries
joels_grade = grades.get("Joel", 0)     # equals 80
print(joels_grade)
kates_grade = grades.get("Kate", 0)     # equals 0
print(kates_grade)
no_ones_grade = grades.get("No One")
print(no_ones_grade)

# assign key/value pair using square bracket
print(grades)
grades["Tim"] = 99                      # replaces the old value
print(grades)
grades["Kate"] = 100                    # adds a third entry
print(grades)
num_students = len(grades)              # equals 3

# dictionarys to represent structured data
tweet = {
    "user" : "joelgrus",
    "text" : "Data science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#sciecne", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()           # iterable for the keys 
print(tweet_keys)
tweet_values = tweet.values()       # iterable for the values
print(tweet_values)
tweet_items = tweet.items()         # itarable for the (key, value) tuples
print(tweet_items)

"user" in tweet_keys                # True, but not pythonic
"user" in tweet                     # pythonic way of checking for keys
"joelgrus" in tweet_values          # True (slow but the only way to check)

# dictionary keys must be "hashable". 



