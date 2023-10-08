
from .blocks.start_end_block import StartEndBlock
from .blocks.straight_road_block import StraightRoadBlock

class Track:

    def __init__(self, start_block, end_block, blocks):
        self.start_block = start_block
        self.end_block = end_block
        self.blocks = blocks

    def draw(self, canvas, T):
        for block in self.blocks:
            block.draw(canvas, T)

    @classmethod
    def straight_line(cls, length, width):
        start = StartEndBlock(0, (0,0), width, True)
        end = StartEndBlock(1, (0,length-1), width, False)
        return Track(start, end, [start, end, StraightRoadBlock(width, length-1, (0,1), True)])
