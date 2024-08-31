from faker import Faker


class PlayerLocallization:
    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            "nick": self.fake.first_name()
        }

    def set_number(self, number=11):
        self.result["number"] = number
        return self

    def build(self):
        return self.result
