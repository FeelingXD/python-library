from enum import Enum


class CommonRe(Enum):
    """
    잘알려진 정규표현식 모음
    """
    def __init__(self,expression:str):
        self.expression = expression

    EMAIL = r"^[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    PHONE_NUMBER = r"^(01[016789]|02|0[3-9][0-9]{1})-[0-9]{3,4}-[0-9]{4}$"
    ...

