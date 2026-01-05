shopping_list = []

while True:
    choice = input("Enter add/remove/show/quit: ").lower()

    if choice == "add":
        item = input("Enter item name: ")
        shopping_list.append(item)

    elif choice == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Item not found")

    elif choice == "show":
        print("Shopping List:", shopping_list)

    elif choice == "quit":
        print("Exiting program")
        break

    else:
        print("Invalid option")
