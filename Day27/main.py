from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=800, height=600)

#  Creating a label
my_label = Label(text="I am a Label", font=("Arial", 15, "bold"))
my_label.pack()

# Creating a button


def button_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)


my_button = Button(text="Click me!", command=button_clicked)
my_button.pack()

# Creating an entry form
user_input = Entry(width=25)

# This code includes some text to begin with
user_input.insert(END, "Type something...")
user_input.pack()

# Textbox

text = Text(height=10, width=30)
text.insert(END, "This is a textbox")

# To get the value in text box, from line 1 character 0
print(text.get("1.0", END))
text.pack()

# Spinbox


def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value.


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton


def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton


def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox


def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()


