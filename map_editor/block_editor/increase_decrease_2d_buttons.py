
from tkinter import *

from .increase_decrease_buttons import IncreaseDecreaseButtons

class IncreaseDecrease2dButtons:

    def __init__(self, master, label_texts=("x","y"), start_values=(4,4), min_values=(1,1), max_values=(None,None), column=0, row=0):
        self.frame = Frame(master)
        self.frame.grid(column=column, row=row)
        self.x_increase_decrease = IncreaseDecreaseButtons(self.frame, label_text=label_texts[0], start_value=start_values[0], min_value=min_values[0], max_value=max_values[0], column=0, row=0)
        self.y_increase_decrease = IncreaseDecreaseButtons(self.frame, label_text=label_texts[1], start_value=start_values[1], min_value=min_values[1], max_value=max_values[1], column=0, row=1)

    def get_value(self):
        return (self.x_increase_decrease.get_value(), self.y_increase_decrease.get_value())
        
