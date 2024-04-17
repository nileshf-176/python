class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found in the list.")

    def view_list(self):
        if self.items:
            print("To-Do List:")
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. {item}")
        else:
            print("Your to-do list is empty.")


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add item\n2. Remove item\n3. View list\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            todo_list.add_item(item)
            print("Item added to the list.")
        elif choice == "2":
            item = input("Enter the item to remove: ")
            todo_list.remove_item(item)
        elif choice == "3":
            todo_list.view_list()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
