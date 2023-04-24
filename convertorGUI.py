from tkinter import *
from convertor_MORSE import ConvertorMorse

class ConvertorGui :

    def __init__(self , master):
        self.master = master
        master.title("MORSE Code Convertor")
        master.config(padx=50, pady=50)

        self.label = Label(master , text="Enter your message:",font=("Arial", 30, "bold"))
        self.label.pack()

        self.entry = Entry(master,width=50)
        self.entry.pack(ipady=3)

        self.button = Button(master , text="Convertor", command=self.convert , pady=8, padx=20 , font=("Arial", 20, "bold"))
        self.button.pack()

        self.output_label = Label(master , text="",font=("Arial", 30, "bold"))
        self.output_label.pack()


    def convert(self):
        user_input = self.entry.get()
        user_input = ConvertorMorse.getInput(user_input)
        user_output = ConvertorMorse.convertor(user_input)
        self.output_label.config(text=user_output)

root =Tk()
morse_gui = ConvertorGui(root)
root.mainloop()
