def min_med_max(x, y, z):
    if x > y > z:
        return [z, y, x]
    if x > z > y:
        return [y, z, x]
    if y > x > z:
        return [z, x, y]
    if y > z > x:
        return [x, z, y]
    if z > y > x:
        return [x, y, z]
    if z > x > y:
        return [y, x, z]
    if x == y == z:
        return [x, y, z]
    if x == y > z:
        return [z, x, y]
    if y == z > x:
        return [x, z, y]
    if x == z > y:
        return [y, x , z]
print(min_med_max(9, 6, 1))
