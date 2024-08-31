from src.enums.user_enums import Statuses

from src.baseclasses.builder import BuilderBaseClass
from src.generators.player_locallization import PlayerLocallization


class Player(BuilderBaseClass):
    def __init__(self):
        super().__init__()
        self.reset()

    def set_status(self, status=Statuses.active.value):
        self.result["account_status"] = status
        return self

    def set_balance(self, balance=0):
        self.result["balance"] = balance
        return self

    def set_avatar(self, avatar="https://yt3.googleusercontent.com/b7z6fCy4B5Gd94k9L4L2op8QID_2Q58cBTai18zx4u2E5GPjgwxgFpvoZOhCe-z1X--6ThI-QKk=s900-c-k-c0x00ffffff-no-rj"):
        self.result["avatar"] = avatar

    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result["locallize"] = {
            "en": PlayerLocallization("en_US").build(),
            "ru": PlayerLocallization("ru_RU").build(),
        }
        return self
