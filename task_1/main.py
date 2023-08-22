from abc import ABC, abstractmethod
from typing import Any

from singletone_logger import Logger


class Calculator(ABC):
    @abstractmethod
    def calculate(self, *args, **kwargs) -> float | int:
        """Calculates according to supported operation types."""
        pass


class BasicCalculator(Calculator):
    """
    Calculator that support basic operation such as:
    - addition
    - subtraction
    - multiplication
    - division
    - floor_division
    - modulo
    """

    def calculate(self, operator: str, a: float, b: float) -> float | int:
        logger.info(f"Calculating: {a} {operator} {b}")
        if operator == "+":
            return self.addition(a, b)
        elif operator == "-":
            return self.subtraction(a, b)
        elif operator == "*":
            return self.multiplication(a, b)
        elif operator == "/":
            return self.division(a, b)
        elif operator == "//":
            return self.floor_division(a, b)
        elif operator == "%":
            return self.modulo(a, b)
        else:
            raise ValueError(
                f"You passed {operator} which is unsupported or invalid operation type."
            )

    def addition(self, a: float, b: float) -> float | int:
        return a + b

    def subtraction(self, a: float, b: float) -> float | int:
        return a - b

    def multiplication(self, a: float, b: float) -> float | int:
        return a * b

    def division(self, a: float, b: float) -> float | int:
        return a / b

    def floor_division(self, a: float, b: float) -> int:
        return a // b

    def modulo(self, a: float, b: float) -> float | int:
        return a % b
    
    def __repr__(self) -> str:
        return "basic calculator"


class AlmightyCalculator:
    """Almighty calculator supports all possible mathematical calculation (in future)."""

    calculator: Calculator = None

    def __init__(self, calculator: Calculator = None) -> None:
        if calculator is not None:
            self.calculator = calculator
        else:
            self.calculator = BasicCalculator()

    def calculate_anything(self, *args, **kwargs) -> float | int | None:
        logger.info(f"Calling {self.calculator} with args={args} and kwargs={kwargs}.")
        if isinstance(self.calculator, BasicCalculator):
            return self.calculator.calculate(*args, **kwargs)
        else:
            logger.info("Currently we support only basic calculator operations.")


if __name__ == "__main__":
    logger = Logger().logger
    basic_calculator = BasicCalculator()

    user = AlmightyCalculator()
    print(user.calculator, BasicCalculator)
    print(user.calculate_anything("-", 4, 5))
