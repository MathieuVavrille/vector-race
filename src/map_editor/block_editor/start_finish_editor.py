
from tkinter import *

from .block_editor import BlockEditor
from .increase_decrease_buttons import IncreaseDecreaseButtons
from track.blocks.start_finish_block import StartFinishBlock

class StartFinishEditor(BlockEditor):

    def __init__(self, master, is_start, buttons_radio, column=0, row=0):
        BlockEditor.__init__(self, master, "Start" if is_start else "Finish", buttons_radio, column, row)
        self.is_start = is_start
        self.width_buttons = IncreaseDecreaseButtons(self.frame, label_text="Width", start_value=4, min_value=1, max_value=None, column=1, row=0)

    def get_block(self, base_coord, turn_level):
        return StartFinishBlock.from_orientation([0,3,1,2][turn_level%4], base_coord, self.width_buttons.get_value(), self.is_start)
