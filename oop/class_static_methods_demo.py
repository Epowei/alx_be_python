# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that adds two numbers.
        
        :param a: First number to add
        :param b: Second number to add
        :return: Sum of a and b
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that multiplies two numbers and prints the calculation type.
        
        :param cls: The class itself, used to access class attributes
        :param a: First number to multiply
        :param b: Second number to multiply
        :return: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
