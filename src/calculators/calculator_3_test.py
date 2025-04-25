from src.calculators.calculator_3 import Calculator3
from pytest import raises

from typing import Dict, List

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriveHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 3

class MockDriveHandler:
    def variance(self, numbers: List[float]) -> float:
        return 10000

def test_calculate_with_variance_error():
    mock_request = MockRequest({ "numbers": [1,2,3,4,5]})
    calculator_3 = Calculator3(MockDriveHandlerError())
    
    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == "Falha no processo: variância menor que a multiplicação"

def test_calculate():
    mock_request = MockRequest({ "numbers": [1,1,1,100]})
    calculator_3 = Calculator3(MockDriveHandler())
    
    response = calculator_3.calculate(mock_request)

    assert response == {'data': {'Calculator': 3, 'value': (10000), 'Success': True}}