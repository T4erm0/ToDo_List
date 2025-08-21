from actions.add_tasks import add_tasks

print("Welcome to ToDo-List")
print("What would you like to do?")
print("1. Add a task")
print("2. Remove a task")

#initialize
task = []

user_input = int(input("Enter your choice: "))

if user_input == 1:
    task = add_tasks()
num_index = len(task)
if task != "":
    for i in range(num_index):
        print(task[i])
else:
    print("You did not enter a task")
