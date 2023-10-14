
from tkinter import *
import numpy as np

from track.blocks.ellipsis_turn_block import EllipsisTurnBlock
from .block_editor import BlockEditor
from .increase_decrease_2d_buttons import IncreaseDecrease2dButtons

class EllipsisTurnEditor(BlockEditor):
    
    def __init__(self, master, buttons_radio, column=0, row=0):
        BlockEditor.__init__(self, master, "Turn", buttons_radio, column, row)
        self.inside_radius_buttons = IncreaseDecrease2dButtons(self.frame, main_text="Inside", label_texts=("x","y"), column=1, row=0, start_values=(2,2))
        self.width_buttons = IncreaseDecrease2dButtons(self.frame, main_text="Widths", label_texts=("x","y"), column=2, row=0)

    def get_block(self, coord, turn_level):
        inside_radius = np.array(self.inside_radius_buttons.get_value())
        return EllipsisTurnBlock(coord,
                                 90*(turn_level%4),
                                 inside_radius,
                                 np.array(self.width_buttons.get_value())+inside_radius-1)
