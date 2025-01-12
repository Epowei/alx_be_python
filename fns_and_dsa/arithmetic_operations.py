def perform_operation(num1: float, num2: float, operation: str) -> float | str:
    """
    Perform a specified arithmetic operation on two numbers.

    :param num1: The first number (float).
    :param num2: The second number (float).
    :param operation: The operation to perform ('add', 'subtract', 'multiply', or 'divide').
    :return: The result of the operation or an error message for division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero error"
        return num1 / num2
    else:
        return "Invalid operation"
