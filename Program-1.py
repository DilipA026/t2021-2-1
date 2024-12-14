class Calculator:
    def __init__(self,a,b,operation):
        self.a=a
        self.b=b
        self.operation=operation
    def perform_operation(self):
        if self.operation == 'add':
            return self.add()
        elif self.operation == 'subtract':
            return self.subtract()
        elif self.operation == 'multiply':
            return self.multiply()
        elif self.operation == 'divide':
            return self.divide()
        else:
            return "Invalid Operation"
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Can't divide by zero"
a = float(input("Enter a value : "))
b = float(input("Enter b value : "))
operation = input("Enter the operation you want to perform (eg. add, subtract, multiply, divide): ").lower()

calculator = Calculator(a, b, operation)

result = calculator.perform_operation()
print(f"Result of {operation} of {a} and {b} is : {result}")