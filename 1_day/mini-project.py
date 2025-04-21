tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t}")
    elif choice == "3":
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            removed = tasks.pop(task_no)
            print(f"Deleted: {removed}")
        else:
            print("Invalid number!")
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
