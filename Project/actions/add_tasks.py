def add_tasks():
    tasks = []
    task_input = ""

    while task_input != "q":
        task_input = input("Enter task(q to quit): ")
        if task_input != "q":
            tasks.append(task_input)
    return tasks