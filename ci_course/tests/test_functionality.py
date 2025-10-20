import ci_course


def test_greet():
    """
    Test the function `greet` in functionality.py
    """
    assert ci_course.greet() == "Hello "
    assert ci_course.greet("Fergus") == "Hello Fergus"


def test_minimum():
    """
    Test the function `minimum` in functionality.py
    """
    assert ci_course.minimum(1, 2, 3) == 1
    assert ci_course.minimum(1.2, 2.3) == 1.2
    assert ci_course.minimum(-1.2, -3) == -3


def test_minimum_with_nonreals():
    """
    Test the function 'minimum' in functionality.py
    with non-real arguments
    """
    assert ci_course.minimum("Foo", "ban", "baz") is None
    assert ci_course.minimum(1j, -3j, -3 + 2j) is None
