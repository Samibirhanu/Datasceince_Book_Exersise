# explore how the values are distrubuted
from collections import Counter
from matplotlib import pyplot as plt

# data 
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 in with the 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
print(histogram)
print(histogram.keys())
print([x + 5 for x in histogram.keys()])

plt.bar([x + 5 for x in histogram.keys()],     # shift bars right by 5
        histogram.values(),                    # Give each bar its correct height 
        10,                                    # give each bar a width of 10
        edgecolor=(0, 0, 0))                   # Black edges for each bar

plt.axis([-5, 105, 0, 5])                      # x-axis from -5 to 105,
                                               # y-axis from 0 to 5

plt.xticks([10 * i for i in range(11)])        # x-axis lables at 0-100
plt.xlabel("Decile")
plt.ylabel("# of studnets")
plt.title("Distribution of Exam 1 Grades")
plt.show()
