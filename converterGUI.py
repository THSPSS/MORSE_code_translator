from tkinter import *
from converter_MORSE import ConverterMorse

class ConverterGui :

    def __init__(self , master):
        self.master = master
        master.title("MORSE Code Translator")
        master.config(padx=50, pady=50)

        self.label = Label(master , text="Enter your message",font=("Arial", 16, "bold"))
        self.label.grid(column=0,row=0)

        self.message_entry = Entry(master,width=30)
        self.message_entry.grid(column=0 , row=1)

        self.morse_entry = Entry(master,width=30)
        self.morse_entry.grid(column=1 , row=1)

        self.error_label = Label(master , text="",font=("Arial", 16))
        self.error_label.grid(column=1, row=2)

        self.button = Button(master , text="Translate", command=self.convert , pady=8, padx=20 , font=("Arial", 20, "bold"))
        self.button.grid(column=0 , row=3)




    def convert(self):
        user_input = self.message_entry.get()
        if len(user_input) == 0:
            self.output_label.config(text="Please enter your message")
            return
        user_output = ConverterMorse.converter(user_input)
        self.morse_entry.insert(index=0,string=user_output)

root =Tk()
morse_gui = ConverterGui(root)
root.mainloop()
