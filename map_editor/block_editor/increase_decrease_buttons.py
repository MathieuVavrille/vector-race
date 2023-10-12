
from tkinter import *

class IncreaseDecreaseButtons():

    def __init__(self, master, label_text="", start_value = 4, min_value=1, max_value=None, column=0, row=0):
        self.label_text = label_text
        self.value = start_value
        self.min_value = min_value
        self.max_value = max_value
        
        self.frame = Frame(master)
        self.frame.grid(column=column, row=row)
        self.label = Label(self.frame)
        self.update_label()
        self.label.grid(column=0, row=0)
        self.decrease = Button(self.frame, text="-", command=self.width_modification(False))
        self.decrease.grid(column=1,row=0)
        self.increase = Button(self.frame, text="+", command=self.width_modification(True))
        self.increase.grid(column=2,row=0)
        
    def update_label(self):
        self.label.config(text=f"{self.label_text} = {self.value}")
        
    def width_modification(self, is_increase):
        def temp():
            self.value += [-1,1][is_increase]
            if self.min_value != None and self.value <= self.min_value:
                self.decrease.config(state="disabled")
            else:
                self.decrease.config(state="normal")
            if self.max_value != None and self.value >= self.max_value:
                self.increase.config(state="disabled")
            else:
                self.increase.config(state="normal")
            self.update_label()
        return temp

    def get_value(self):
        return self.value
