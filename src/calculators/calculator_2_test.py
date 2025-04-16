from .calculator_2 import Calculator2
from typing import Dict

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    Mock_Request = MockRequest({ "numbers": [2.12, 4.62, 1.32]})

    calculator_2 = Calculator2()
    calculator_2.calculate(Mock_Request)