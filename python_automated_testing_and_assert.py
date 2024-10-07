# Using assert statment, will cause AssertionError
assert 1 + 1 == 3, "1 + 1 should equal 2 but didn't"

def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 40]) == 5
assert smallest_item([1, 0, -1, 2]) == -1

Assert inputs to functions
def smallest_item(xs):
    assert xs, "empty list has no smallest item"
    return min(xs)

smallest_item([])           