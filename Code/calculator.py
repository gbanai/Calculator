"""Calculator calculates the basic mathematical operations as
addition, subtraction, multiplication, division and n-root.
Calculator performs actions with a value inside its memory.
It means that the first number is in the calculator memory,
the second number is selected when calling the function"""

class Calculator:
    def __init__(self):
        self.memory = 0
        self.total = 0

    def addition(self, number):
        if isinstance(number, int) or isinstance(number, float):
            self.number = number
            self.total = self.memory + self.number
            self.memory += self.number
            return self.total
        else:
            print('Wrong type of input is selected')
        return self.total

    def subtraction(self, number):
        if isinstance(number, int) or isinstance(number, float):
            self.number = number
            self.total = self.memory - self.number
            self.memory = self.total
        else:
            print('Wrong type of input is selected')
        return self.total

    def multiplication(self, number):
        if isinstance(number, int) or isinstance(number, float):
            self.number = number
            self.total = self.memory * self.number
            self.memory = self.total
        else:
            print('Wrong type of input is selected')
        return self.total

    def division(self, number):
        if isinstance(number, int) or isinstance(number, float):
            self.number = number
            if number == 0:
                return False
            else:
                self.total = self.memory / self.number
                self.memory = self.total
        else:
            print('Wrong type of input is selected')
        return self.total

    def root(self, number):
        if isinstance(number, int) or isinstance(number, float):
            self.number = number
            if number % 2 == 0 and self.memory > 0:
                self.total = self.memory ** (1 / self.number)
                self.memory = self.total
            else:
                return False
        else:
            print('Wrong type of input is selected')
        return self.total

    def reset(self):
        """Function resets calculation memory"""
        self.memory = 0
        return self.memory
