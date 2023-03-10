import tkinter

window = tkinter.Tk()
window.title('Miles to kilometres program')
window.minsize(width=500, height=500)
window.config(padx=40, pady=40)  # add padding ton window widget


# Buttons
def convert_miles_to_km():
    km = float(miles) * 1.60934


# Label

label = tkinter.Label(text='I am label', font=('Arial', 40, 'bold'))
# label.pack(expand=True)  # places component on page at center
label.place(x=0, y=0)  # place shown in specified location

# can do label['text'] to chagne the text or use config


# Entry/INput

input_miles = tkinter.Entry()
input_miles.pack()
miles = input_miles.get()

button = tkinter.Button(text="Click to convert", command=convert_miles_to_km)

# button.grid(column=0, row=0), this is the start then with next widget use .grid and add a columns number bigger than 0 / row > 0

window.mainloop()

# layout managers pack place and grid, pack defaults to top down approach, can change using side keyword
