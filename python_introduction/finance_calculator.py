# This script will calculate the user’s monthly savings based on inputted monthly income and expenses.

monthly_income = input("Enter your monthly income:")

monthly_expenses = input("Enter your monthly expenses:")

monthly_income = int(monthly_income)
monthly_expenses = int(monthly_expenses)

monthly_savings = monthly_income - monthly_expenses

projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}")

print(f"Projected savings after one year, with interest, is: ${projected_savings}")
