number1 = 10  # Global variable
number2 = 20  # Global variable

def summation():  # Function definition
    number3 = 50  # Local variable defined inside the function
    result = number1 + number2 + number3  # Summing global and local variables
    print(result)  # Printing the result


def subtraction():
    result = number1 - number2
    print(result)

def multiplication():
    result = number1 * number2
    print(result)

def division():
    result = number1 / number2
    print(result)

summation()


