def safe_divide(numerator, denominator):
    try:
        #Convert the string inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        try:
            #division operation
            result = num / den
            return f"The result of the division is {result}"
            
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
            
    except ValueError:
        return "Error: Please enter numeric values only."