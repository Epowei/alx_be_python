
def daily_reminder():
    # Prompt for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Validate priority input
    match priority:
        case "high":
            priority_message = "a high priority task"
        case "medium":
            priority_message = "a medium priority task"
        case "low":
            priority_message = "a low priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            return

    # Check if the task is time-sensitive
    if time_bound == "yes":
        time_message = "that requires immediate attention today!"
    elif time_bound == "no":
        time_message = "Consider completing it when you have free time."
    else:
        print("Invalid input for time sensitivity. Please enter yes or no.")
        return

    # Provide the customized reminder
    print(f"Reminder: '{task}' is {priority_message} {time_message}")

# Run the function
daily_reminder()

