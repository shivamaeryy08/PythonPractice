from tkinter import *

window = Tk()
window.title('Convert miles to kilometres')
window.minsize(width=400, height=100)
window.config(pady=40, padx=30)
miles_label = Label(text='Miles', font=('Arial', 10))
miles_label.grid(column=2, row=0)
km_label = Label(text='Km', font=('Arial', 10))
km_label.grid(column=2, row=1)
equal_to_label = Label(text='is equal to', font=('Arial', 10))
equal_to_label.grid(column=0, row=1)


def convert_miles_to_km():
    input_miles = miles.get()
    print(input_miles)
    try:
        input_miles = float(input_miles)
    except ValueError:
        print("Enter a valid number")
        return

    kilometres = input_miles * 1.609
    km.insert(0, f"{kilometres}")


miles = Entry()
miles.grid(column=1, row=0)
km = Entry()
km.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
