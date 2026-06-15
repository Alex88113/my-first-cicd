import pytest

from calculate import Add, Sub

class TestAdd:
    """ Success tests """
    @pytest.mark.parametrize("value1, value2, expected", [
        (100, 100, 200),
        (1000, 2900, 3900),
        (549, 100, 649),
        (320, 421, 741)
    ])

    def test_add(self, value1, value2, expected) -> None:
        add = Add(value1, value2)

        assert add.add_numbers() == expected
        assert isinstance(add.add_numbers(), float | int)
        assert add.add_numbers() > 0

    """ Exception tests """
    @pytest.mark.parametrize("bag1, bag2", [
        (-1, 0),
        ("", -1212),
        (None, ''),
        (-12, None)
    ])

    def test_exception(self, bag1, bag2) -> None:
        with pytest.raises(ValueError):
            Add(bag1, bag2)

class TestSub:
    """ Success tests """
    @pytest.mark.parametrize('value1, value2, expected', [
        (100, 23, 77),
        (903, 800, 103),
        (1212, 90, 1122),
        (323, 78, 245)
    ])

    def test_sub_method(self, value1, value2, expected) -> None:
        sub = Sub(value1, value2)
        assert sub.sub_numbers() == expected


    """ Exception tests """
    @pytest.mark.parametrize("bag1, bag2", [
        (-1, 0),
        ("", -1212),
        (None, ''),
        (-12, None)
    ])

    def test_exception_sub(self, bag1, bag2) -> None:
        with pytest.raises(ValueError):
            Sub(bag1, bag2)