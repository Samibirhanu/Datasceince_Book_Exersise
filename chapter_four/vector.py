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

