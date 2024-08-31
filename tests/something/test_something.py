import pytest
from src.generators.player_locallization import PlayerLocallization
from src.enums.user_enums import Statuses


@pytest.mark.parametrize("status", [
    *Statuses.list()
])
def test_something(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "avatar",
    "locallize",
    "avatar",
])
def test_something1(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


@pytest.mark.parametrize("locallizations, loc", [
    ("fr", "fr_FR")
])
def test_something2(get_player_generator, locallizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ["locallize", locallizations], PlayerLocallization(
            loc).set_number(7).build()
    ).build()
    print(object_to_send)
