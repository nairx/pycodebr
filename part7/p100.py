from tkinter import *
root = Tk()

def handleSubmit():
    name = entry.get()
    message = Label(root,text="Hello "+name)
    message.place(relx=0.05,rely=0.2)

root.geometry("800x600")
root.option_add("*Font","ariel 20 bold")
root.title("My Application")
label = Label(root,text="Name")
label.place(relx=0.05,rely=0.05)
entry = Entry(root)
entry.place(relx=0.2,rely=0.05)
button = Button(root,text="Submit",command=handleSubmit)
button.place(relx=0.6,rely=0.04)
root.mainloop()

