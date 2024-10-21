from python_defaultdict import document
# counter turn a sequance of values into a defaultdict(int)- like object mapping keys to counts:
from collections import Counter
c = Counter([0, 1, 2, 0])           # c is basically {0: 2, 1: 1, 2: 1}
print(c)

# very simple way to solve our word_counts problem
word_counts = Counter(document)     # create dictionary with each word count
print(word_counts)

# most_common method returns n most common elements and their counts
for word, count in word_counts.most_common(10):         # prints 10 most common words and their counts
    print(word, count)
print(word_counts)


