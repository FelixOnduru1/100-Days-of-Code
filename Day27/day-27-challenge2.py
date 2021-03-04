from tkinter import *
window = Tk()
window.title("Practicing Grid")
window.minsize(width=800, height=600)
window.config(padx=20, pady=20)

my_label = Label(text="I am a Label", font=("Arial", 15, "bold"))
my_label.grid(column=0, row=0)

my_button = Button(text="button")
my_button.grid(column=1, row=1)

new_button = Button(text="new button")
new_button.grid(column=2, row=0)

user_input = Entry()
user_input.grid(column=3, row=3)
window.mainloop()
