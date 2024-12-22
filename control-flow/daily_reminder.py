# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority and time sensitivity
match priority:
    case "high":
        reminder_start = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder_start = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder_start = f"Note: '{task}' is a low priority task"
    case _:
        reminder_start = f"Reminder: '{task}' has an unrecognized priority"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder = f"{reminder_start} that requires immediate attention today!"
else:
    reminder = f"{reminder_start}. Consider completing it when you have free time."

# Output the reminder
print(reminder)

