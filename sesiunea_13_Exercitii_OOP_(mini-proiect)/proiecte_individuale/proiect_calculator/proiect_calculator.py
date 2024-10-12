import math
# todo: rezolvarea erorilor de "Invalid operation" atunci cand calculez, **, //.


class MiniCalculator:
    def __init__(self, initial_value=0):
        """Initialize the calculator with a default initial value."""
        self.current_value = initial_value

    def add(self, number):
        """Add a number to the current value."""
        result = self.current_value + number
        print(f"{self.current_value} + {number} = {result}")
        self.current_value = result
        return self.current_value

    def subtract(self, number):
        """Subtract a number from the current value."""
        result = self.current_value - number
        print(f"{self.current_value} - {number} = {result}")
        self.current_value = result
        return self.current_value

    def multiply(self, number):
        """Multiply the current value by a number."""
        result = self.current_value * number
        print(f"{self.current_value} * {number} = {result}")
        self.current_value = result
        return self.current_value

    def divide(self, number):
        """Divide the current value by a number."""
        if number == 0:
            print("Error: Division by zero.")
            return self.current_value
        result = self.current_value / number
        print(f"{self.current_value} / {number} = {result}")
        self.current_value = result
        return self.current_value

    def modulus(self, number):
        """Calculate the modulus of the current value by a number."""
        result = self.current_value % number
        print(f"{self.current_value} % {number} = {result}")
        self.current_value = result
        return self.current_value

    def floor_divide(self, number):
        """Floor divide the current value by a number."""
        if number == 0:
            print("Error: Division by zero.")
            return self.current_value
        result = self.current_value // number
        print(f"{self.current_value} // {number} = {result}")
        self.current_value = result
        return self.current_value

    def power(self, number):
        """Raise the current value to the power of a number."""
        result = self.current_value ** number
        print(f"{self.current_value} ** {number} = {result}")
        self.current_value = result
        return self.current_value

    def square_root(self):
        """Calculate the square root of the current value."""
        if self.current_value < 0:
            print("Error: Cannot compute the square root of a negative number.")
            return self.current_value
        result = math.sqrt(self.current_value)
        print(f"√{self.current_value} = {result}")
        self.current_value = result
        return self.current_value

    def set_value(self, number):
        """Set the current value to a specific number."""
        self.current_value = number
        print(f"Current value set to: {self.current_value}")
        return self.current_value

    def reset(self):
        """Reset the current value to zero."""
        self.current_value = 0
        print("Calculator reset to zero.")
        return self.current_value

    def display(self):
        """Display the current value."""
        return self.current_value


def main():
    import sys

    # Check if an initial value is provided via command line arguments
    if len(sys.argv) > 1:
        try:
            initial_value = float(sys.argv[1])
        except ValueError:
            print("Invalid initial value. Setting to 0.")
            initial_value = 0
    else:
        initial_value = 0

    # Create an instance of MiniCalculator
    calculator = MiniCalculator(initial_value)
    print(calculator.display())  # Display the initial value

    while True:
        # Prompt user for input
        user_input = input("> ")

        # Exit the program if the user types 'x'
        if user_input.lower() == 'x':
            break

        # Reset the calculator if the user types 'delete'
        if user_input.lower() == 'reset':
            calculator.reset()
            continue

        # Determine the operation based on the first character
        if user_input.startswith('+'):
            try:
                number = float(user_input[1:])
                calculator.add(number)
            except ValueError:
                print("Invalid operation")
        elif user_input.startswith('-'):
            try:
                number = float(user_input[1:])
                calculator.subtract(number)
            except ValueError:
                print("Invalid operation")
        elif user_input.startswith('*'):
            try:
                number = float(user_input[1:])
                calculator.multiply(number)
            except ValueError:
                print("Invalid operation")
        elif user_input.startswith('/'):
            try:
                number = float(user_input[1:])
                calculator.divide(number)
            except ValueError:
                print("Invalid operation")
        elif user_input.startswith('%'):
            try:
                number = float(user_input[1:])
                calculator.modulus(number)
            except ValueError:
                print("Invalid operation")
        elif user_input.startswith('//'):
            try:
                number = float(user_input[2:])
                calculator.floor_divide(number)
            except ValueError:
                print("Invalid operation")
        elif user_input.startswith('**'):
            try:
                number = float(user_input[2:])
                calculator.power(number)
            except ValueError:
                print("Invalid operation")
        elif user_input.startswith('='):
            try:
                number = float(user_input[1:])
                calculator.set_value(number)
            except ValueError:
                print("Invalid operation")
        elif user_input.startswith('√'):
            calculator.square_root()
        else:
            print("Invalid operation")


if __name__ == "__main__":
    main()
