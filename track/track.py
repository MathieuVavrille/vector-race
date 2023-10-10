
from .blocks.start_end_block import StartEndBlock
from .blocks.straight_road_block import StraightRoadBlock

class Track:

    def __init__(self, start_block, end_block, blocks):
        self.start_block = start_block
        self.end_block = end_block
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
        start = StartEndBlock(0, (0,0), width, True)
        end = StartEndBlock(1, (0,length-1), width, False)
        return Track(start, end, [start, end, StraightRoadBlock(width, length-2, (0,1), True)])
        
    @classmethod
    def straight_line_horizontal(cls, length, width):
        start = StartEndBlock(3, (0,0), length, True)
        end = StartEndBlock(2, (width-1,0), length, False)
        return Track(start, end, [start, end, StraightRoadBlock(width-2, length, (1,0), False)])
