import streamlit as st
import functions

# Get list of to-do items
toDos = functions.get_todos()

# Define function to add to-do each time we write it in the app
def add_todo():
    toDo = st.session_state["newToDo"] + '\n'
    toDos.append(toDo)
    functions.write_todos(toDos)


st.title("My To Do App")
st.subheader("Organize your day.")
st.write('Add items on your to-do list below')

# Get list of to-dos from file
toDos = functions.get_todos()

for index, toDo in enumerate(toDos):
    checkboxTrue = st.checkbox(toDo, key=toDo)

    if checkboxTrue:
        toDos.pop(index)
        functions.write_todos(toDos)
        del st.session_state[toDo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter new to-do here", on_change=add_todo, key='newToDo')
