from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        # todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            print(f"{index + 1} - {item.capitalize().strip("\n")}")

    elif user_action.startswith("edit"):
        try:
            # Get the number of the list to edit
            number = int(user_action[5:])

            todos = get_todos()

            new_todo = input("Enter a new todo: ").capitalize()
            todos[number - 1] = new_todo

            # Write the new todos to the txt file
            write_todos(todos)

            print("Your todos has been updated...")
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todos.pop(number - 1)

            write_todos(todos)

            print("To do removed from list...")
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid!")

print("Bye!")