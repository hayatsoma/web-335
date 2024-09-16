"""
Author: Hayat Soma
Date: 2024-09-15
File Name: Soma_lemonadeStandSchedule.py
Description: This program manages a weekly schedule for a lemonade stand. It includes tasks related to running the stand and displays the tasks for each day of the week.
"""

# Defining a list of tasks related to running the lemonade stand
tasks = [
    "Buy lemons",
    "Make lemonade",
    "Sell lemonade",
    "Count earnings",
    "Clean up"
]

# Printing the list of tasks
print("Tasks for running the lemonade stand:")
for task in tasks:
    print(task)

# Defining a list of days of the week
days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

# Printing the task for each day of the week
print("\nWeekly Schedule:")
for i, day in enumerate(days):
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: It's a day off, you should rest.")
    else:
        # Use modulo operator to loop through tasks if there are more days than tasks
        task = tasks[i % len(tasks)]
        print(f"{day}: Task for the day - {task}")
