
from tkinter import *

from track.blocks.straight_road_block import StraightRoadBlock
from .block_editor import BlockEditor
from .increase_decrease_2d_buttons import IncreaseDecrease2dButtons

class StraightRoadEditor(BlockEditor):
    
    def __init__(self, master, buttons_radio, column=0, row=0):
        BlockEditor.__init__(self, master, "Straight", buttons_radio, column, row)
        self.dimension_buttons = IncreaseDecrease2dButtons(self.frame, main_text = "Dimension", label_texts=("Width","Height"), column=2, row=0)

    def get_block(self, coord, turn_level):
        value = self.dimension_buttons.get_value()
        return StraightRoadBlock.from_position(value[0], value[1], coord, turn_level%2==0)
