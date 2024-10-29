from collections.abc import Iterable
from typing import Union


def quadratic_roots(a: int, b: int, c: int) -> Iterable[Union[int | float] | str]:
    # your code here
    x1 = (-1 * b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-1 * b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    if type(x1) == complex or type(x2) == complex:
        return ["No real roots"]
    else:
        return sorted([x1, x2], reverse=True)


print("Example:")
print(list(quadratic_roots(1, 2, 3)))

# These "asserts" are used for self-checking
assert list(quadratic_roots(1, -3, 2)) == [2, 1]
assert list(quadratic_roots(1, 0, -1)) == [1, -1]
assert list(quadratic_roots(1, 2, 1)) == [-1, -1]
assert list(quadratic_roots(1, 0, 1)) == ["No real roots"]
assert list(quadratic_roots(1, 4, 4)) == [-2, -2]
assert list(quadratic_roots(1, -5, 6)) == [3, 2]
assert list(quadratic_roots(1, -6, 9)) == [3, 3]
assert list(quadratic_roots(2, 2, 1)) == ["No real roots"]
assert list(quadratic_roots(2, -7, 6)) == [2, 1.5]
assert list(quadratic_roots(2, -3, 1)) == [1, 0.5]

print("The mission is done! Click 'Check Solution' to earn rewards!")
