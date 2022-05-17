from pickletools import pyset
import pytest

from SSN_Validator import SSNValidation

@pytest.mark.parametrize(
    "number, expected",
    [
        ("000-25-6302", False),
        ("666-25-6302", False),
        ("920-25-6302", False),
        ("250-25-6302", True),
        ("250-00-9520", False),
        ("250-20-9520", True),
        ("250-20-0000", False),
        ("250-20-5000", True),
        ("250*20*5000", False),
        ("Juan Gabriel", False)
    ]
)
def test_SSNValidation(number, expected):
    assert SSNValidation(number) == expected