class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

    def get_number(self, message):
        while True:
            try:
                value = float(input(message))
                return value
            except ValueError:
                print("Invalid input! Enter a valid number.")

    def menu(self):
        print("\n--- MENU ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Enter your choice: ")

            if choice == '5':
                print("Goodbye!")
                break

            num1 = self.get_number("Enter first number: ")
            num2 = self.get_number("Enter second number: ")

            if choice == '1':
                print(f"ADD : {num1} + {num2} = {self.add(num1, num2)}")

            elif choice == '2':
                print(f"Subtract : {num1} - {num2} = {self.subtract(num1, num2)}")

            elif choice == '3':
                print(f"Multiply : {num1} * {num2} = {self.multiply(num1, num2)}")

            elif choice == '4':
                print(f"Divide : {num1} / {num2} = {self.divide(num1, num2)}")

            else:
                print("Invalid choice! Try again.")


calc = Calculator()
calc.run()
