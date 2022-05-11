from email import message
from tkinter import *

from mysqlx import ColumnType

# class ProcessButtonEvent:
#     def __init__(self) :
#         window = Tk()
#         btOk = Button(window, text="Ok", fg = "red", command= self.processOK)
#         btCancel = Button(window, text="Cancel", bg="yellow", command=self.processCancel)
#         btOk.pack()
#         btCancel.pack()

#         window.mainloop()
    
#     def processOK(self):
#         print("Ok button is clicked")
#     def processCancel(self):
#         print("Cancel button is clicked")

# ProcessButtonEvent()

# class WidgetsDemo:
#     def __init__(self):
#         window = Tk()
#         window.title("Widgets Demo")

#         frame1 = Frame(window)
#         frame1.pack()
#         self.v1 = IntVar()
#         cbtBold = Checkbutton(frame1, text="Bold",variable=self.v1, command=self.processCheckbutton)
#         self.v2 = IntVar()
#         rbRed = Radiobutton(frame1, text="Red", bg="red", variable=self.v2, value=1, command=self.processRadiobutton)
#         rbYellow = Radiobutton(frame1, text="Yellow", bg = "yellow", variable=self.v2, value = 2, command=self.processRadiobutton)

#         cbtBold.grid(row=1, column=1)
#         rbRed.grid(row=1, column=2)
#         rbYellow.grid(row=1, column= 3)

#         frame2 = Frame(window)
#         frame2.pack()
#         label = Label(frame2, text="Enter your name : ")
#         self.name = StringVar()
#         entryName = Entry(frame2, textvariable=self.name)
#         btGetName = Button(frame2, text="Get Name", command=self.processButton)
#         message = Message(frame2, text="It is a widgets demo")
#         label.grid(row=1, column = 2)
#         entryName.grid(row=1, column = 2)
#         btGetName.grid(row=1, column = 3)
#         message.grid(row = 1, column=4)

#         text = Text(window)
#         text.pack()
#         text.insert(END, "Tip\nThe best way to learn Tkinter is to read")
#         text.insert(END, "these carefully designed examples and use them ")
#         text.insert(END, "to create your applications. ")

#         window.mainloop()
    
#     def processCheckbutton(self):
#         print("check button is " + ("checked" if self.v1.get() == 1 else "unchecked"))

#     def processRadiobutton(self):
#         print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected ")

#     def processButton(self):
#         print("Your name is " + self.name.get())

# WidgetsDemo()

# class GridMangerDemo :
#     window = Tk()
#     window.title("Grid Manager Demo")

#     message = Message(window, text="This Message widget occupies three rows and two columns")
#     message.grid(row=1, column=1, rowspan=3, columnspan=2)
#     Label(window, text="First name :").grid(row=1, column= 3)
#     Entry(window).grid(row=1, column=4, padx=5, pady=5)
#     Label(window, text="Last name : ").grid(row=2, column=3)
#     Entry(window).grid(row=2, column=4)
#     Button(window, text="Get Name").grid(row=3, padx=5, pady=5, column=4, sticky=E)
#     window.mainloop()
# GridMangerDemo()

class PackManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("Pack Manager Demo 1")

        Label(window, text="Blue", bg="blue").pack(side=LEFT)
        Label(window, text="Red", bg = "red").pack(side=LEFT,fill=BOTH,expand=1)
        Label(window, text="Green", bg="green").pack(side=LEFT, fill=BOTH)
        
        window.mainloop()
PackManagerDemo()