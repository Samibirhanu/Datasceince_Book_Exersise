# matrics is two dimentional collection of numbers.
from typing import List, Tuple, Callable


Matrix = List[List[float]]
Vector = List[float]

def shape(A:Matrix) -> Tuple[int, int]:
    """Retuns (# of rows of A, # of colomns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0               # number of elements in first row
    return num_rows, num_cols
assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)     # 2 rows, 3 columns

# retuns a row of a matrics
def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i] 
assert get_row([[1, 2, 3], [4, 5, 6]], 0) == [1, 2, 3] 

# returns a colomn of matrices
def get_column(A: Matrix, j:int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return[A_i[j] for A_i in A]
assert get_column([[1, 2, 3], [4, 5, 6]], 2) == [3, 6] 

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols matrix 
    whose (i, j)-th entry_fn(i, j)
    """
    return [[entry_fn(i, j)                 #  given i, create a list
             for j in range(num_cols)]      #  [entry-fn(i, 0), ...]
            for i in range(num_rows)]      #  create one list for each i

def add(i: int, j: int) -> float:
    return i + j
matrix = make_matrix(3, 3, add)
print (matrix)

# create identitiy matrix
def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i,j: 1 if i == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]

friendships =[(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
              (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#            user 0  1  2  3  4  5  6  7  8  9
#
friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],        # user 1
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],        # user 2
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],        # user 3
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],        # user 4
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],        # user 5
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],        # user 6
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],        # user 7
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],        # user 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]        # user 9

assert friend_matrix[0][2] == 1, "0 and 2 are friends"
assert friend_matrix[0][8] == 0, "0 and 8 are not friends"
