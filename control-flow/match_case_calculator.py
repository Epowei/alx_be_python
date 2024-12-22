# match_case_calculator.py

# Prompt user for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt for operation
operation = input("Choose the operation (+, -, *, /): ")

# Use match-case for operation selection
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            result = None  # To prevent further use of result
        else:
            result = num1 / num2
    case _:
        print("Invalid operation selected.")
        result = None

# Output the result
if result is not None:
    print(f"The result is {result}.")
