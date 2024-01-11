import tkinter

window = tkinter.Tk()
window.title("Hello world TKinter")
window.minsize(width=500, height=300)

#label

my_label = tkinter.Label(text="Label abc", font=("Arial", 24))
my_label.pack(side= "bottom")






window.mainloop()
