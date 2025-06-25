def todo_list():
    tasks = []

    while True:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter new task: ")
            tasks.append(task)
        elif choice == '2':
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f'Removed task: {removed}')
            else:
                print("Invalid task number.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

todo_list()
