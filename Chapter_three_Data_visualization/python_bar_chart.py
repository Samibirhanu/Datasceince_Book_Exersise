# bar charts used to show how some quantity varies among some discrete set of items.
from matplotlib import pyplot as plt
# data shows how many academy awards were won by each of a varity of movies:
movies = ["Annie Hall", "Ben-hur", "Casablanca", "Gandhi", "West side story"]
num_oscars = [5, 11, 3, 8, 10]

# plot bar with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies")     # add a title
plt.ylabel("# of Academy Awards")   # label the y-axis

# label x-axis with movie names at bar centers
plt.xticks(range(len(movies)), movies)

# Display
plt.show()