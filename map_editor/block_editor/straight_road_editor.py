
from tkinter import *

from .block_editor import BlockEditor
from .increase_decrease_2d_buttons import IncreaseDecrease2dButtons

class StraightRoadEditor(BlockEditor):
    
    def __init__(self, master, buttons_radio, column=0, row=0):
        BlockEditor.__init__(self, master, "Straight", buttons_radio, column, row)
        self.label = Label(self.frame, text="Dimension")
        self.label.grid(column=1,row=0)
        self.dimension_buttons = IncreaseDecrease2dButtons(self.frame, label_texts=("Width","Height"), column=2, row=0)
                                                           
