from .calculator_2 import Calculator2
from typing import Dict
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriveHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: list[float]) -> float:
        return 3


def test_calculate_integration():
    Mock_Request = MockRequest({ "numbers": [2.12, 4.62, 1.32]})

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    formated_response = calculator_2.calculate(Mock_Request)

    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 2, "result": 0.08}}

def test_calculate():
    Mock_Request = MockRequest({ "numbers": [2.12, 4.62, 1.32]})

    driver = MockDriveHandler()
    calculator_2 = Calculator2(driver)
    formated_response = calculator_2.calculate(Mock_Request)

    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 2, "result": 0.33}}