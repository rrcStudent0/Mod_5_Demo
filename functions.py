"""
Description: Module 05 demonstration: Functions
Author: {student name}
Date: {current date}
Usage: To run individual functions, place a function 
call within the main guard.
"""

def greet()->None:
    """
    Prints a Hello World Message.
    
    """
    print("Hullo Wrld!") 

def greet_name_age(name: str, age: int) -> None:
    """
    Prints a greeting icluding name and age.

    Args:
        name (str): The name of the person being greeted
        age (int): The age of the person being greeted.

    """
    print(f"Hello {name} you are {age} years old.")


def math_operations(operand1: int, 
                    operand2: int, 
                    operation:str = "+") -> float:
    """
    Returns the result of the addition or subtraction 
    math operation. Defualts to addition if an operation
    os not provided

    Args:
        operand1 (int): Left operand
        operand2 (int): Right operand
        operation (str): Default = "+"
                        Symbol represenring math operation

    Returns:
        float: The result of the math operation.  

    Raise:
        ValueError: When operation is not + or -.
    """

    if operation == "+":
        result = operand1 + operand2
    elif operation == "-":
        result = operand1 - operand2
    else:
        raise ValueError("Invalid Operation.")
    return float(result)



# greet()
# greet()
# greet()

# greet_name_age("Isaiah", 25)

# Avoid placing multiple statments into
# a try/except if it is not necessary.
# try:
#     print(math_operations(1, 5, "-"))
#     print(math_operations(10, 10, "+"))
#     print(math_operations(30, 30, "*"))
# except ValueError as e:
#     print(e)

try:
    print(math_operations(10, 10, "*"))
except ValueError as e:
    print(e)
try:
    print(math_operations(1, 3, "+"))

except ValueError as e:
    print(e)
try:
    print(math_operations(4, 6, "-"))
except ValueError as e:
    print(e)

try:
    print(math_operations(99, 10))
except ValueError as e:
    print(e)

# print(math_operations.__doc__)

# print(help(math_operations))

print("one, two, buckle my shoe, three four, want some more.")





















