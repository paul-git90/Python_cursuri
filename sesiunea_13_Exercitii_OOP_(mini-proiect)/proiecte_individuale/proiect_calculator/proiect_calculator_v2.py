import math
import sys

"""
Operatii:
+, -, *, /, **=sq, //=flat, %, √=rad
"""


class MiniCalculator:
    def __init__(self, initial_value=0):
        self.current_value = initial_value

    def add(self, number):
        self.current_value += number
        return self.current_value

    def subtract(self, number):
        self.current_value -= number
        return self.current_value

    def multiply(self, number):
        self.current_value *= number
        return self.current_value

    def divide(self, number):
        if number != 0:
            self.current_value /= number
            return self.current_value
        else:
            return "Cannot divide by zero"

    def set_value(self, number):
        self.current_value = number
        return self.current_value

    def floor_divide(self, number):
        if number != 0:
            self.current_value //= number
            return self.current_value
        else:
            return "Cannot divide by zero"

    def modulus(self, number):
        self.current_value %= number
        return self.current_value

    def power(self, number):
        self.current_value **= number
        return self.current_value

    def square_root(self):
        if self.current_value < 0:
            return "Cannot calculate square root of a negative number"
        self.current_value = math.sqrt(self.current_value)
        return self.current_value

    def reset(self):
        self.current_value = 0
        return self.current_value


def main():
    initial_value = 0
    if len(sys.argv) > 1:
        try:
            initial_value = float(sys.argv[1])
        except ValueError:
            print("Invalid initial value. Using default value 0.")

    calculator = MiniCalculator(initial_value)

    print(calculator.current_value)  # Display initial value
    while True:
        user_input = input("> ")

        if user_input.startswith("+"):
            number = float(user_input[1:])
            previous_value = calculator.current_value
            result = calculator.add(number)
            print(f"{previous_value} + {number} = {result}")

        elif user_input.startswith("-"):
            number = float(user_input[1:])
            previous_value = calculator.current_value
            result = calculator.subtract(number)
            print(f"{previous_value} - {number} = {result}")

        elif user_input.startswith("*"):
            number = float(user_input[1:])
            previous_value = calculator.current_value
            result = calculator.multiply(number)
            print(f"{previous_value} * {number} = {result}")

        elif user_input.startswith("/"):
            number = float(user_input[1:])
            previous_value = calculator.current_value
            result = calculator.divide(number)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{previous_value} / {number} = {result}")

        elif user_input.startswith("="):
            number = float(user_input[1:])
            result = calculator.set_value(number)
            print(f"Setting value to {number}. Current value is now {result}")

        elif user_input.startswith("flat"):  # Floor division
            number = float(user_input[5:])  # Extracting number after "flat "
            previous_value = calculator.current_value
            result = calculator.floor_divide(number)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{previous_value} // {number} = {result}")

        elif user_input.startswith("%"):
            number = float(user_input[1:])  # Modulus operation
            previous_value = calculator.current_value
            result = calculator.modulus(number)
            print(f"{previous_value} % {number} = {result}")

        elif user_input.startswith("sq"):  # Power operation
            number = float(user_input[3:])  # Extracting number after "sq "
            previous_value = calculator.current_value
            result = calculator.power(number)
            print(f"{previous_value} ** {number} = {result}")

        elif user_input.startswith("rad"):  # Square root operation
            previous_value = calculator.current_value
            result = calculator.square_root()
            if isinstance(result, str):
                print(result)
            else:
                print(f"√{previous_value} = {result}")

        elif user_input.lower() == "reset":
            print("Calculator reset to zero.")

        elif user_input.lower() == "x":
            break

        else:
            print("Invalid operation")

        print(calculator.current_value)


if __name__ == "__main__":
    main()
