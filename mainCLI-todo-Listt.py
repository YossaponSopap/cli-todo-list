messageDisplay = "\n***** To-Do List Application *****\n" \
    "1. Add Task\n" \
    "2. Delete Task\n" \
    "3 View Task\n" \
    "4 Quit\n"

tasks = []
def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("task added successfully.")

def del_task():
        if len(tasks) == 0:
            print("No task to delete!")
        else:
            print("Task:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

            choice = int(input("Enter task number to delete."))
            if 0 < choice <= len(tasks):
                del tasks[choice-1]
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")

def view_taskS():
        if len(tasks) == 0:
            print("No task!")
        else:
            print("List of task")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

while True:   
    print(messageDisplay)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        del_task()
    elif choice == 3:
        view_taskS()
    elif choice == 4:
        print("Thank you! for using To-Do-List Application")
        break
    else:
        print("nothing, try again")