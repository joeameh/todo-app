import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")

add_button_exit = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label, input_box, add_button],
                           [add_button_exit]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
    elif event == "Exit":
        break
    print(event)
    print(values)

window.close()


