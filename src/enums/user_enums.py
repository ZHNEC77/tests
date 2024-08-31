from enum import Enum
from src.baseclasses.pyenum import PyEnum


class Genders(Enum):
    female = 'female'
    male = 'male'


class Statuses(PyEnum):
    inactive = 'inactive'
    active = 'active'
    ban = "ban"
    delete = "delete"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain '@'"
