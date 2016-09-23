"""Square root with different methods."""

def square_root_with_newton_method(number, iterations):
    """
    :param number: Number we take root from.
    :param iterations: How many times we repeat action.
    :return: Return root with Newton method.
    """
    g = number / 2
    for x in range (0, iterations):
        g = (g + number / g) / 2
    rounded_root1 = "%.3f" % g
    return rounded_root1

def square_root_with_exp_ln(number):
    """
    :param number:
    :return:
   """
    number = number**(1/2)
    rounded_root2 = "%.3f" % number
    return rounded_root2

def square_root_result(number, iterations):
    """
    Please describe here the content of this function, parameters and returnable value.
    :param number:
    :param iterations:
    :return:
    """
    newton_root = square_root_with_newton_method(number, iterations)
    normal_root = square_root_with_exp_ln(number)
    print("Ruutjuur " + str(number) + "-st: " + "Newtoni meetod " + "(iter: " + str(iterations) + "): " + str(newton_root) +
    "; exp-ln: " + str(normal_root))
    return 0
square_root_result(7, 2)
