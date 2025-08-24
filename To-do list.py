class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"✅ Task added: {task}")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"✔ Task completed: {self.tasks[index]['task']}")
        else:
            print("❌ Invalid task number!")

    def show_tasks(self):
        if not self.tasks:
            print("📌 No tasks in the list!")
            return
        print("\n📋 To-Do List:")
        for i, t in enumerate(self.tasks, start=1):
            status = "✅ Done" if t["completed"] else "⏳ Pending"
            print(f"{i}. {t['task']} - {status}")


todo = ToDoList()

while True:
    print("\n1. Add Task\n2. Mark Task Completed\n3. Show Tasks\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo.add_task(task)

    elif choice == "2":
        num = int(input("Enter task number to mark as completed: ")) - 1
        todo.mark_completed(num)

    elif choice == "3":
        todo.show_tasks()

    elif choice == "4":
        print("👋 Exiting To-Do List. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Try again.")
