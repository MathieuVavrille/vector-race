
import numpy as np

from .road_block import RoadBlock
from constants import BORDER_OFFSET

class StartFinishBlock(RoadBlock):

    def __init__(self, is_vertical, is_left_or_up, start_pos, width, is_start):
        """orientation: 0=up, 1=down, 2=left, 3=right;
        left_or_down_position is the position of the start of the block (bottommost or leftmost, knowing that it is inverted on canvas);
        width is the width of the block, should be > 0 (it is the number of starting positions)."""
        self.is_vertical = is_vertical
        self.is_left_or_up = is_left_or_up
        self.start_pos = left_or_down_position
        self.width = width
        self.is_start = is_start
        self.compute_edges()

    def compute_edges(self):
        invert_value = 1 if self.is_left_or_up else -1
        if self.is_vertical:
            self.start_or_finish = (self.start_pos+[-BORDER_OFFSET,0],self.start_pos+[self.width-1+BORDER_OFFSET,0])
            self.side1 = (self.start_pos+[-BORDER_OFFSET,0],self.start_pos+[-BORDER_OFFSET,invert_value*BORDER_OFFSET])
            self.side2 = (self.start_pos+[self.width-1+BORDER_OFFSET,invert_value*BORDER_OFFSET],self.start_pos+[self.width-1+BORDER_OFFSET,0])
        else:
            self.start_or_finish = (self.start_pos+[0,-BORDER_OFFSET],self.start_pos+[0,self.width-1+BORDER_OFFSET])
            self.side1 = (self.start_pos+[0,-BORDER_OFFSET],self.start_pos+[invert_value*BORDER_OFFSET,-BORDER_OFFSET])
            self.side2 = (self.start_pos+[invert_value*BORDER_OFFSET,self.width-1+BORDER_OFFSET],self.start_pos+[0,self.width-1+BORDER_OFFSET])
    
    def check(self, x, y):
        if self.is_vertical:
            return self.start_pos[0]==x and self.start_pos[1] <= y < self.left[1]+self.width
        else:
            return self.start_pos[0] <= x < self.left[0] and self.left[1] == y

    def draw(self, canvas, T, linewidth):
        canvas.create_line(T(self.start_or_finish[0]),T(self.start_or_finish[1]),
                           width=linewidth,fill="green" if self.is_start else "red")
        canvas.create_line(T(self.side1[0]), T(self.side1[1]),
                           T(self.side2[0]), T(self.side2[1]),
                           width=linewidth)

    def list_positions(self):
        """The positions allowed by the block are on the start/finish line"""
        if self.is_vertical:
            return {(self.start_pos[0]+i, self.start_pos[1]) for i in range(self.width)}
        else:
            return {(self.start_pos[0], self.start_pos[1]+i) for i in range(self.width)}

    def to_json(self):
        return {"block_style": "StartFinishBlock",
                "is_vertical": self.is_vertical,
                "is_letf_or_up": self.is_left_or_up,
                "start_pos": tuple(self.start_pos),
                "width": self.width,
                "is_start": self.is_start}

    @classmethod
    def from_orientation(cls, orientation, left_or_down_position, width, is_start):
        return StartFinishBlock(self.is_vertical = orientation <= 1, orientation in {1,2}, left_or_down_position, width, is_start)

    
    def __repr__(self):
        return f"{'Start' if self.is_start else 'Finish'}({['right','left','up','down'][self.is_vertical*2+self.is_left_or_up]},{self.start_pos},{self.width})"
