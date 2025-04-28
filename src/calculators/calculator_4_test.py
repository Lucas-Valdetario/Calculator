from src.calculators.calculator_4 import Calculator4
from pytest import raises
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculator():
    # Usa uma lista em vez de um conjunto
    mock_request = MockRequest({"numbers": [13, 15, 16, 54]})
    calculator_4 = Calculator4(NumpyHandler())

    response = calculator_4.calculate(mock_request)

    # Verifica a estrutura
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Verifica o cálculo da média
    expected_mean = (13 + 15 + 16 + 54) / 4  # = 24.5
    assert response["data"]["result"] == expected_mean

