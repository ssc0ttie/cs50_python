from unitest_calculator import square

# test categorically


def test_square():
    assert square(2) == 4
    assert square(-2) == 4
    assert square(3) == 9
    assert square(-3) == 9
    assert square(0) == 0


# this will give you more clues on the summary of the test
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0
