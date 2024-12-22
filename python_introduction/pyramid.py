rows = 5

# Initialize the row counter
row = 0

# Outer loop for rows
while row < rows:
    # Initialize the space counter
    spaces = rows - row - 1
    # Inner loop for spaces before the asterisks
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    
    # Initialize the asterisk counter
    asterisks = 2 * row + 1
    # Inner loop for printing asterisks
    while asterisks > 0:
        print("*", end="")
        asterisks -= 1
    
    # Move to the next line after each row
    print()
    row += 1
