from actions.add_tasks import add_tasks

print("Welcome to ToDo-List")
print("What would you like to do?")
print("1. Add a task")
print("2. Remove a task")

user_input = int(input())

if user_input == 1:
    task = add_tasks()

print(task)

