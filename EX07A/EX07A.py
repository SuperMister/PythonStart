def min_med_max(x, y, z):
    """Compare 3 numbers and give maximum, minimum and median.

    :param x: First number.
    :param y: Second number.
    :param z: Third number.
    :return: Return list of numbers where first number is minimum, second is median and third is maximum
    """
    if x >= y and x >= z:
        if y >= z:
            return [z, y, x]
        if z >= y:
            return [y, z, x]
    if y >= x and y >= z:
        if x >= z:
            return [z, x, y]
        if z >= x:
            return [x, z, y]
    if z >= x and z >= y:
        if x >= y:
            return [y, x, z]
        if y >= x:
            return [x, y, z]
print(min_med_max(7, 2, 2))
