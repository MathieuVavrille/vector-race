
from tkinter import *

from .block_editor.start_finish_editor import StartFinishEditor
from .block_editor.straight_road_editor import StraightRoadEditor
from .block_editor.radio_button_behaviour import RadioButtonBehaviour

class BlockSelection(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master, borderwidth = 5, relief="groove")
        self.grid(column=1,row=0)
        main_buttons_radio = RadioButtonBehaviour()
        self.all_blocks = [StartFinishEditor(self, True, main_buttons_radio, column=0, row=0),
                           StartFinishEditor(self, False, main_buttons_radio, column=0, row=1),
                           StraightRoadEditor(self, main_buttons_radio, column=0, row=2)]

    def get_block(self, coord, turn_level):
        for block in self.all_blocks:
            if block.is_active():
                return block.get_block(coord, turn_level)

    
                                             
