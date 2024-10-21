# sample document
document = ["apple", "banana", "apple", "orange", "banana", "apple"]
# Count the word in a document
word_counts = {}                # create empty dictionary
for word in document:           # looping through the document
    if word in word_counts:     # checking if the word is already in the dictionary
        word_counts[word] += 1  # updating the count for the existing words
    else:                       
        word_counts[word] = 1   # adding new words to the dictionary with value 1
print(word_counts)

# "forgivness is better than permission" approach using exception
word_counts_2 = {}               # create empty dictionary
for word in document:           # looping through the document
    try:                        # try block tries to increment the cont for the word
        word_counts_2[word] += 1 
    except KeyError:            # keyError occures when the word is not found in the dictionary
        word_counts_2[word] = 1
print(word_counts_2) 

# Third approach using get, which behaves gracefully
word_count_3 = {}
for word in document:
    previous_count = word_count_3.get(word, 0)
    print(previous_count)
    word_count_3[word] = previous_count + 1
print(word_count_3)

# forth approch using default dict
# import defaultdict from collections module
from collections import defaultdict 

word_count_4 = defaultdict(int)      # int() produce 0 creates dictionary
for word in document:                # looping though the document 
    word_count_4[word] +=1           # appending each word count            
print(word_count_4)

# usefull for list
dd_list = defaultdict(list)         # list() produces an empty list
dd_list[2].append(1)                # now dd_list contains {2: [1]}
print(dd_list)
# usefull also for dict
dd_dict = defaultdict(dict)         # dict() produces an empty dict
dd_dict["Joel"]["city"] = "seattle" # {"Joel" : {"city: Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                      # now dd_pair contains {2: [0, 1]}
print(dd_pair)

# usful when we are using dicitionaries to "collect" results by some key and dont want to have to check every time to see if the key exists yet.
