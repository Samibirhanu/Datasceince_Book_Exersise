from matplotlib import pyplot as plt
# right choice for visualizing the relationship between two paired sets of data. 
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
lables = ['a', 'b', 'c', 'd', 'e', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends,minutes)

# label each point
for label, friend_count, minute_count in zip(lables, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),           # put the label with its point
                 xytext=(5,-5),                             # but slightly offset
                 textcoords='offset points'                 
                 )
plt.title("Daily minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spend on the site")
plt.show()