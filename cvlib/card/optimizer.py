from typing import Callable, TypeVar

from cvlib.typing import Number


T = TypeVar('T', int, Number)


def bound_optimization(
    x0: T,
    x1: T,
    f: Callable[[T], Number],
    limit: Number,
    tolerance: Number = 1,
    mid_transform: Callable[[Number], T] = lambda x: x
):

    bounds = [x0, x1]
    values = [f(b) for b in bounds]

    while (bounds[1] - bounds[0]) > tolerance:
        mid = mid_transform(sum(bounds) / 2)
        mid_value = f(mid)

        idx = int(mid_value > limit)
        bounds[idx] = mid
        values[idx] = mid_value

    return bounds[0]
