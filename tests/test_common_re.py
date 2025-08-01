import re
import pytest
from rehelper.common_re import CommonRe


def test_email_regex():
    """EMAIL 정규식 테스트"""
    # Positive cases
    assert re.match(CommonRe.EMAIL.value, "test@example.com")
    assert re.match(CommonRe.EMAIL.value, "user.name+tag@gmail.co.uk")
    assert re.match(CommonRe.EMAIL.value, "12345@snu.ac.kr")

    # Negative cases
    assert not re.match(CommonRe.EMAIL.value, "test@.com")
    assert not re.match(CommonRe.EMAIL.value, "test@domain")
    assert not re.match(CommonRe.EMAIL.value, "test@domain.")
    assert not re.match(CommonRe.EMAIL.value, "@domain.com")
    assert not re.match(CommonRe.EMAIL.value, "test@domain..com")


def test_phone_number_regex():
    """PHONE_NUMBER 정규식 테스트"""
    # Positive cases
    assert re.match(CommonRe.PHONE_NUMBER.value, "010-1234-5678")
    assert re.match(CommonRe.PHONE_NUMBER.value, "02-123-4567")
    assert re.match(CommonRe.PHONE_NUMBER.value, "031-1234-5678")

    # Negative cases
    assert not re.match(CommonRe.PHONE_NUMBER.value, "010-123-456")
    assert not re.match(CommonRe.PHONE_NUMBER.value, "123-4567-8901")
    assert not re.match(CommonRe.PHONE_NUMBER.value, "01012345678")
    assert not re.match(CommonRe.PHONE_NUMBER.value, "010-1234-56789")