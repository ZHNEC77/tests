from enum import Enum


class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = "Recived status code is not equal to expected"
    WRONG_ELEMENT_COUNT = "Number of item not equal to expected"
