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


def quntile(xs: List[float], p: float) -> float:
    """Returns the pth-percentile value in x"""
    p_index = int(p *len(xs))
    return sorted(xs)[p_index]
quntile(num_friends, 0.10) == 25

# measures of spread  Range
def data_range(r: List[float]) -> float:
    """Returns the range value of list"""
    sorted_range = sorted(r)
    return (sorted_range[-1] - sorted_range[0])
assert data_range([1, 2, 3, 4, 5, 6]) == 5, 'your function is not correct'


# variance
def variance(v: List[float]) -> float:
    """Returns the variance of data list my trial"""
    mean_v = mean(v)                           # find mean
    # print(mean_v)
    dist_mean = [(i - mean_v)**2 for i in v]   # find distance between the mean from all data points
    n = len(dist_mean)
    variance = sum(dist_mean)/ (n - 1)
    return variance
sample = variance([1, 2, 3, 4, 5])
print(sample)

Vector = List[List[float]]

def dot(v:Vector, w:Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * W_n"""
    assert len(v) == len(w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return  dot(v, v)

def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by substracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x -x_bar for x in xs ]

def variance_joel(xs: List[float] ) -> float:
    """Almost the averaage squared deviation from the mean"""
    assert len(xs) >= 2, "variance requirs at least two elements"

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)
# assert variance_joel([1, 2, 3, 4, 5]) == 2

print(variance([2.74, 1.23, 2.63, 2.22, 3, 1.98]))
print(variance_joel([2.74, 1.23, 2.63, 2.22, 3, 1.98]))

import math
def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    return math.sqrt(variance_joel(xs))

# print(standard_deviation([1, 2, 3, 4, 5])) 

# interquartile_range 
def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and the 25%-tile"""
    return quntile(xs, 0.75) - quntile(xs, 0.25)

print(interquartile_range([1,2,3,4,5,6,7,8,9]))
