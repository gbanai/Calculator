# Calculator
Calculator package perfoms basic mathematical operations:

-addition (a+b) <br />
-subtraction (a-b) <br />
-multiplication (a*b) <br />
-division (a/b) <br />
-(n) root of a number (a^(1/b))<br />

Calculator performs actions with a value inside its memory.

# Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install calculator

```python
pip install git+https://github.com/gbanai/Calculator.git
```
# Example

```python
from Code.calculator import Calculator
calc = Calculator()
calc.addition(5) # returns 5
calc.multiplication(3) # returns 15
calc.subtraction(3) # returns 12
calc.division(3) # returns 4
print(calc.root(2)) # returns 2
```
