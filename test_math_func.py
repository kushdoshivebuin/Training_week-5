import math_func
import pytest

# @pytest.mark.number
# def test_add():
#     assert math_func.add(5, 5) == 10
#     assert math_func.add(10, 2) == 12

# @pytest.mark.number
# def test_product():
#     assert math_func.product(5, 5) == 25
#     assert math_func.product(5) == 10

# @pytest.mark.strings
# def test_add_strings():
#     assert math_func.add("Hello", " World") == "Hello World"

# @pytest.mark.strings
# def test_product_strings():
#     assert math_func.product("Hello") == "HelloHello"


@pytest.mark.parametrize('num1, num2, result',
                        [
                             (7, 3, 10),
                             ('Hello', ' World', 'HelloWorld'),
                             (10.5, 25.5, 36),
                        ]
                        )
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result
