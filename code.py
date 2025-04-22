class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Додано завдання: {task}")

    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.")
        else:
            print("\nСписок завдань:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Завдання '{removed_task}' виконано і видалено.")
        else:
            print("Невірний номер завдання.")

def main():
    todo = ToDoList()

    while True:
        print("\nМеню:")
        print("1. Додати завдання")
        print("2. Показати список завдань")
        print("3. Видалити завдання")
        print("4. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            task = input("Введіть нове завдання: ")
            todo.add_task(task)
        elif choice == "2":
            todo.show_tasks()
        elif choice == "3":
            todo.show_tasks()
            try:
                task_number = int(input("Введіть номер завдання для видалення: "))
                todo.remove_task(task_number)
            except ValueError:
                print("Будь ласка, введіть число.")
        elif choice == "4":
            print("Вихід...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
