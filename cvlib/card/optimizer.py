
def bound_optimization(x0, x1, f, limit,
                       tolerance=1, mid_transform=lambda x: x):
    bounds = [x0, x1]
    values = [f(b) for b in bounds]

    while (bounds[1] - bounds[0]) > tolerance:
        mid = mid_transform(sum(bounds) / 2)
        mid_value = f(mid)

        idx = int(mid_value > limit)
        bounds[idx] = mid
        values[idx] = mid_value

    return bounds[0]
