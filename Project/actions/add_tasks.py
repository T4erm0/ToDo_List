def add_tasks():
    total_tasks = [] #For the Task list
    task_input = "" #Initializing it here beforehand

    while task_input != "q":
        task_input = input("Enter task(q to quit): ")
        if task_input != "q":
                total_tasks.append(task_input)
    return total_tasks