class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not isinstance(task, str) or not task.strip():
            raise ValueError("Task must be a non-empty string.")
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, task_index):
        if not isinstance(task_index, int) or not (0 <= task_index < len(self.tasks)):
            raise IndexError("Invalid task index.")
        self.tasks[task_index]["completed"] = True

    def delete_task(self, task_index):
        if not isinstance(task_index, int) or not (0 <= task_index < len(self.tasks)):
            raise IndexError("Invalid task index.")
        del self.tasks[task_index]

    def get_tasks(self):
        return self.tasks

def main():
    todo_list = TodoList()
    print("Welcome to your To-Do List!")

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Complete a task")
        print("3. Delete a task")
        print("4. View tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task description: ")
            try:
                todo_list.add_task(task)
                print(f"Task '{task}' added.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '2':
            try:
                index = int(input("Enter the index of the task to complete: "))
                todo_list.complete_task(index)
                print("Task marked as completed.")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
        elif choice == '3':
            try:
                index = int(input("Enter the index of the task to delete: "))
                todo_list.delete_task(index)
                print("Task deleted.")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
        elif choice == '4':
            tasks = todo_list.get_tasks()
            if not tasks:
                print("No tasks in the list.")
            else:
                print("\nYour Tasks:")
                for i, task_item in enumerate(tasks):
                    status = "[X]" if task_item["completed"] else "[ ]"
                    print(f"{i}. {status} {task_item['task']}")
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
