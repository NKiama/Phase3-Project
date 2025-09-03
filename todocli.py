from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo

def show():
    todos = get_all_todos()
    print("\nTodos:")
    for i, todo in enumerate(todos, start=1):
        done = "Done" if todo.status == 2 else "Not Done"
        print(str(i) + ". " + todo.task + " | " + (todo.category or "No Category") + " | " + done)
    print()

def main():
    while True:
        print("1. Add todo")
        print("2. Delete todo")
        print("3. Update todo")
        print("4. Complete todo")
        print("5. Show todos")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Task: ")
            category = input("Category: ")
            insert_todo(task, category)
            show()
        elif choice == "2":
            pos = int(input("Todo number to delete: ")) - 1
            delete_todo(pos)
            show()
        elif choice == "3":
            pos = int(input("Todo number to update: ")) - 1
            new_task = input("New task (leave blank to skip): ")
            new_cat = input("New category (leave blank to skip): ")
            update_todo(pos, new_task or None, new_cat or None)
            show()
        elif choice == "4":
            pos = int(input("Todo number to complete: ")) - 1
            complete_todo(pos)
            show()
        elif choice == "5":
            show()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
