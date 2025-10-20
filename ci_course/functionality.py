import numbers


def greet(name=""):
    """
    A function that takes a name and returns a greeting.

    :param name: The name to greet, defaults to ""
    :type name: str|""
    :return: The greeting
    :rtype: str
    """
    return f"Hello {name}"


def minimum(*args):
    r"""
    A function taking some arguments and returning the minimum number among the arguments.

    :param \*args: The numbers from which to return the minimum
    :type \*args: int|float
    :return: The minimum
    :rtype: int|float
    """
    if not any([isinstance(arg, numbers.Real) for arg in args]):
        return

    the_min = float("inf")
    for arg in args:
        if isinstance(arg, numbers.Real):
            the_min = min(the_min, arg)

    return the_min
