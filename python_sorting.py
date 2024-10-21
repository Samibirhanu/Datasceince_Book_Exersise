# sorting list
x = [4, 1, 2, 3]
y = sorted(x)       # y is [1, 2, 3, 4]
print(y)
x.sort()            # now x is [1, 2, 3, 4]
print(x)

# sort the list by absolute value from larhest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)       # is [-4, 3, -2, 1]
print (x)

word_counts = {'apple': 3, 'banana': 2, 'cherry': 5}
wc = sorted(word_counts.items(),                             # This converts the word_counts dictionary into a list of tuples contain (word and count)
            key = lambda word_and_count: word_and_count[1],  #  specifies the sorting criteria. using lambda function 
            reverse=True)                                    # specifies order of sort which is desending order
print(wc)
