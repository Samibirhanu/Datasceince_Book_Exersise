# vector is just a list of floats:
from typing import List

Vector = List[float]

# vector addition
def add(v:Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "victors must be the same lenth"
    return [v_i + w_i for v_i, w_i in zip(v,w)]
assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

# vector substraction
def substract(v:Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "victors must be the same lenth"
    return [v_i - w_i for v_i, w_i in zip(v,w)]
assert substract([4, 5, 6], [1, 2, 3]) == [3, 3, 3]

def vector_sum(vectors:List[Vector]) -> Vector:
    """Sums all corresponding elemets"""
    # Check that vectors is not empety
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all (len(v) == num_elements for v in vectors), "different sizes!"

    # the i-th elements of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

# multipliying vector by scalar
def scalar_multiply(c: float, v:Vector) -> Vector:
    """Multiplies every element by c"""
    return [c *v_i for v_i in v]
assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

# means of a list of (same-sized) vetors:
def vector_mean(vectors:List[Vector]) -> Vector:
    """Computes the elements-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

# dot product 
def dot(v:Vector, w:Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * W_n"""
    assert len(v) == len(w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))
assert dot([1,2,3], [4, 5, 6]) == 32

def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return  dot(v, v)
assert sum_of_squares([1, 2, 3]) == 14      # 1 * 1 + 2 * 2 + 3 * 3

# calculating magnitide
import math

def magnitude(v: Vector) -> float:
    """Returns the magnitude (or lenght) of v"""
    return math.sqrt(sum_of_squares(v))     # math.square root function
assert magnitude([3, 4]) == 5

# distance between two vectors
def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) **2 + ... (v_n - w_n) ** 2"""
    return sum_of_squares(substract(v, w))
def distance(v : Vector, w: Vector) -> float:
    """"Computes (v_1 -w_1)**2 + ... + (v_n - w_n) ** 2"""
    return math.sqrt(squared_distance(v, w))

# equvalence of distance
def distance2(v: Vector, w: Vector) -> float:
    return magnitude(substract(v, w))

