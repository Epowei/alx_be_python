# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print the current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date(days):
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date by adding the timedelta
    future_date = current_date + timedelta(days=days)
    # Format and print the future date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Main execution
if __name__ == "__main__":
    display_current_datetime()
    
    # Prompt user for input
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    calculate_future_date(days_to_add)
