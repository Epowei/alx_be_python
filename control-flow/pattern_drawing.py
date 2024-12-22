
# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern
row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # This will print a newline after each row
    row += 1
