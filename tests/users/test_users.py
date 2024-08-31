import pytest
from src.baseclasses.response import Response
from src.pydentic_chemas.user import User
from src.pydentic_chemas.computer import Computer

from examples import computer
# URL = 'https://my-json-server.typicode.com/typicode/demo/posts'


def test_getting_user_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    # print(make_number)


@pytest.mark.productions
@pytest.mark.skip("[ISSUE-23414] Issue with network connected")
def test_another():
    """
    In this test we to try check that 1 is equal to 1
    """
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize("first_value, second_value, result", [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ("b", "a", None),
    ("b", -2, None),
])
def test_calculator(first_value, second_value, result, calculate):
    """
    In this test we are calculated with different values(Valid and invalid)
    """
    assert calculate(first_value, second_value) == result


def test_pydantic_object():
    comp = Computer.model_validate(computer)

    print(comp.detailed_info)
