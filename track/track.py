
import numpy as np

from .blocks.start_finish_block import StartFinishBlock
from .blocks.straight_road_block import StraightRoadBlock
from .blocks.ellipsis_turn_block import EllipsisTurnBlock

class Track:

    def __init__(self, start_block, finish_block, blocks):
        self.start_block = start_block
        self.finish_block = finish_block
        self.blocks = blocks
        
        self.allowed_positions = set()
        for block in self.blocks:
            self.allowed_positions.update(block.list_positions())
        self.start_positions = self.start_block.list_positions()

    def draw(self, canvas, T, linewidth):
        for block in self.blocks:
            block.draw(canvas, T, linewidth)

    def get_allowed_positions(self):
        return self.allowed_positions
        
    @classmethod
    def straight_line_vertical(cls, length, width):
        start = StartFinishBlock(0, np.array([0,0]), width, True)
        finish = StartFinishBlock(1, np.array([0,length-1]), width, False)
        return Track(start, finish, [start, finish, StraightRoadBlock(width, length, (0,0), True)])
        
    @classmethod
    def straight_line_horizontal(cls, length, width):
        start = StartFinishBlock(3, np.array([0,0]), length, True)
        finish = StartFinishBlock(2, np.array([width-1,0]), length, False)
        return Track(start, finish, [start, finish, StraightRoadBlock(width, length, (0,0), False)])

    @classmethod
    def one_turn(cls):
        start = StartFinishBlock(0, np.array([0,0]), 4, True)
        finish = StartFinishBlock(1, np.array([7,7]), 2, False)
        return Track(start, finish, [start, finish,
                                  EllipsisTurnBlock(np.array([6,0]), 90, np.array([3,2]),np.array([6,4])),
                                  EllipsisTurnBlock(np.array([6,7]), 270, np.array([1,3]),np.array([2,5]))])
        

