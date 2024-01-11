from tkinter import *

window = Tk()
window.title("Hello world TKinter")
window.minsize(width=500, height=300)

#label

my_label = Label(text="Label abc", font=("Arial", 24))
my_label.pack()

my_label["text"] = "new text"
my_label.config(text="text v3")

#button

def button_clicked():

    button.config(text="Done")
    button.config(state="disabled")
    user_input = input.get()
    my_label.config(text=f"Button Confirm clicked + {user_input} ")
    print(user_input)


button = Button(text="Confirm", command=button_clicked)
button.pack()

#Entry component,
# basically is a input component
input = Entry(width=10)
input.pack()


window.mainloop()
