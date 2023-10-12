
from tkinter import *

class BlockEditor:

    def __init__(self, master, main_button_label, buttons_radio, column=0, row=0):
        self.frame = Frame(master)
        self.frame.grid(column=column, row=row)
        self.main_button = Button(self.frame, text=main_button_label)
        self.main_button.grid(column=0,row=0, sticky="nesw")
        buttons_radio.append(self.main_button)

    def is_active(self):
        return self.main_button["relief"] == "sunken"
