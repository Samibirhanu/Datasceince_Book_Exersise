from collections import Counter
import matplotlib.pyplot as plt
from typing import List


num_friends = [100, 49, 41, 40, 25]
friend_counts = Counter(num_friends)

xs = range(101)
ys = [friend_counts[x] for x in xs]

# plt.bar(xs, ys)
# plt.axis([0, 101, 0, 25])
# plt.title("Histogram of Friend Counts")
# plt.xlabel('# of friends')
# plt.ylabel("# of people")
# plt.show()

# mean/ average
def mean(xs:List[float]) -> float:
    """returns the mean of list of values"""
    return sum(xs) / len(xs)
assert mean([1, 2, 3, 4, 5]) == 3, 'the mean function is not correct'

print(mean(num_friends))                # 51.0

# median
def _median_odd(xs: List[float]) -> float:
    """if len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]
assert _median_odd([1, 2, 3, 4, 5]) == 3, 'the median is not correct'

def _median_even(xs: List[float]) -> float:
    """if len(xs) is even, the median is the sum of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2    # e.g length 4 ==> hi_midpoint 2
    return (sorted_xs[hi_midpoint -1] + sorted_xs[hi_midpoint]) / 2      
assert _median_even([1, 2, 3, 4, 5 ,6]) == 3.5, 'median even is not equal'

def median(v: List[float]) -> float:
    """finds the middle-most value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)
assert median([1,2,3,4,5,6,7]) == 4
assert median([8, 1, 4, 5, 6, 9]) == 5.5

# Mode
def mode(x: List[float]) -> List[float]:
    """Returns a list, since there might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]
print(mode([1,9,3,4,3,3,4,6,77,6,96,9,4,9,4,3,0,0]))
