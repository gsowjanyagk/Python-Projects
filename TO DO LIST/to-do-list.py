print("-"*75)
print("                              TO-DO LIST")
print("-"*75)
print("Please select an option:")
print("1. Add a task")
print("2. View tasks")
print("3. Mark task as complete")
print("4. Exit")
print("-"*75)
while True: 
    opt = input("Enter your choice (1-4): ")
    def add():
        task = input("Enter the task: ")
        with open("TO DO LIST/task.txt", "a") as file:
            file.write(task + "\n")
        print(f"Task '{task}' added successfully!")
    def view():
        print("-"*75)
        print("Your tasks:")
        with open("TO DO LIST/task.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
        print("-"*75)
    def complete():
        view()
        try:
            task_num = int(input("Enter the task number to mark as complete: "))

            with open("TO DO LIST/task.txt", "r") as file:
                tasks = file.readlines()

            if 1 <= task_num <= len(tasks):
                completed_task = tasks.pop(task_num - 1)

                with open("TO DO LIST/task.txt", "w") as file:
                    file.writelines(tasks)

                print(f"Completed: {completed_task.strip()}")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid task number.")
    if opt == "1":
        add()
    elif opt == "2":
        view()
    elif opt == "3":
        complete()
    elif opt == "4":
        print("-"*75)
        print("                              Thank you!")
        print("-"*75)
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")
        continue
    print("-"*75)