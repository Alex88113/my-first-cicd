class Add:
    def __init__(
            self, number1: int | float,
            number2: int | float) -> None:
        if not isinstance(number1,  int | float):
            raise ValueError("type a number1 add class is incorrect")

        if number1 < 0:
            raise ValueError("number1 is negative")

        self.number1 = number1

        if not isinstance(number2,  int | float):
            raise ValueError("type a number2 add class is incorrect")

        if number2 < 0:
            raise ValueError("number2 is negative")

        self.number2 = number2

    def add_numbers(self) -> float:
        return self.number1 + self.number2

class Sub:
    def __init__(
            self, number1: int | float,
            number2: int | float) -> None:
        if not isinstance(number1, int | float):
            raise ValueError("type a number1 add class is incorrect")

        if number1 < 0:
            raise ValueError("number1 is negative")

        self.number1 = number1

        if not isinstance(number2, int | float):
            raise ValueError("type a number2 add class is incorrect")

        if number2 < 0:
            raise ValueError("number2 is negative")

        self.number2 = number2

    def sub_numbers(self) -> int:
        return self.number1 - self.number2
