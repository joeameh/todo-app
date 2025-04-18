import functions
import FreeSimpleGUI as sg
import time

#sg.theme("Green")

clock = sg.Text(key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(40, 10))
edit_button = sg.Button("Edit")

add_button_exit = sg.Button("Exit")

complete_button = sg.Button("Complete")

window = sg.Window('My To-Do App',
                   layout=[[clock], [label, input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [add_button_exit]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo.capitalize())
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'].capitalize()
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Please select an item first",
                     font=("helvetica", 20))
    elif event == "todos":
        item = values['todos'][0]
        window['todo'].update(value=item)

    elif event == "Complete":
        try:
            todo_completed = values['todos'][0]
            todos = functions.get_todos()
            index = todos.index(todo_completed)
            todos.pop(index)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        except IndexError:
            sg.popup("Please select an item first",
                   font=("helvetica", 20))
    elif event == "Exit":
        break
    print(event)
    print(values)

window.close()
