"""Square root with different methods."""


def square_root_with_newton_method(number, iterations):
    """Take root from number with Newton method.

    :param number: Number we take root from.
    :param iterations: How many times we repeat action.
    :return: Return root with Newton method.
    """
    g = number / 2
    for x in range(0, iterations):
        g = (g + number / g) / 2
    rounded_root1 = round(g, 3)
    return rounded_root1


def square_root_with_exp_ln(number):
    """Take root with exp method.

    :param number: Number we want root from.
    :return: Return root with logarithm method.
   """
    number **= (1 / 2)
    rounded_root2 = round(number, 3)
    return rounded_root2


def square_root_result(number, iterations):
    """Print both results.

    :param number: Number we take root from.
    :param iterations: How many times we repeat action in first function.
    :return: Return text with 2 answers.
    """
    newton_root = square_root_with_newton_method(number, iterations)
    normal_root = square_root_with_exp_ln(number)
    return ("Ruutjuur " + str(number) + "-st: " + "Newtoni meetod " +
            "(iter: " + str(iterations) + "): " + str(newton_root) +
            "; exp-ln: " + str(normal_root))

print(square_root_result(99.69, 3))
