from Calculator.Calculator import addition
from Calculator.Calculator import subtraction
from Calculator.Calculator import multiplication
from Calculator.Calculator import division
from Calculator.Calculator import squared
from Calculator.Calculator import squarerooted

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = squared(a)
        return self.result

    def squareroot(self, a):
        self.result = squarerooted(a)
        return self.result