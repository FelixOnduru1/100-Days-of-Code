from tkinter import *
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

miles = Entry(width=8)
miles.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 12))
equal_label.grid(column=0, row=1)

km_number_label = Label(text="0", font=("Arial", 12, "bold"))
km_number_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)


def button_clicked():
    num_miles = float(miles.get())
    num_km = round(num_miles * 1.60934, 2)

    km_number_label.config(text=f"{num_km}")


calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()
