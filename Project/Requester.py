from actions.add_tasks import add_tasks

def menu():
    user_input = ""
    tasks = []
    while user_input != 4:
        print("What would you like to do?")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Show all tasks")
        print("4. Exit")

        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            new_items = add_tasks()
            tasks.extend(new_items)
        elif user_input == 2:
            pass

        elif user_input == 3:
 #           if tasks == None:
 #               print("You don't have any tasks yet")
 #           else:
                print(f"Your tasks are:")
                for i in range(len(tasks)):
                    print(tasks[i])

        elif user_input == 4:
            exit()

        else:
            print("You did not enter a valid choice.")