
import numpy as np

from .road_block import RoadBlock
from constants import BORDER_OFFSET

class StartFinishBlock(RoadBlock):

    class_name="StartFinishBlock"

    def __init__(self, is_vertical=True, is_left_or_down=True, start_pos=np.array([0,0]), width=4, is_start=True, **kwargs):
        """
        left_or_down_position is the position of the start of the block (bottommost or leftmost, knowing that it is inverted on canvas);
        width is the width of the block, should be > 0 (it is the number of starting positions)."""
        self.is_vertical = is_vertical
        self.is_left_or_down = is_left_or_down
        self.start_pos = start_pos
        self.width = width
        self.is_start = is_start
        self.compute_edges()

    def compute_edges(self):
        invert_value = 1 if self.is_left_or_down else -1
        if self.is_vertical:
            self.start_or_finish = (self.start_pos+[-BORDER_OFFSET,0],self.start_pos+[self.width-1+BORDER_OFFSET,0])
            self.side1 = (self.start_pos+[-BORDER_OFFSET,0],self.start_pos+[-BORDER_OFFSET,invert_value*BORDER_OFFSET])
            self.side2 = (self.start_pos+[self.width-1+BORDER_OFFSET,invert_value*BORDER_OFFSET],self.start_pos+[self.width-1+BORDER_OFFSET,0])
        else:
            self.start_or_finish = (self.start_pos+[0,-BORDER_OFFSET],self.start_pos+[0,self.width-1+BORDER_OFFSET])
            self.side1 = (self.start_pos+[0,-BORDER_OFFSET],self.start_pos+[invert_value*BORDER_OFFSET,-BORDER_OFFSET])
            self.side2 = (self.start_pos+[invert_value*BORDER_OFFSET,self.width-1+BORDER_OFFSET],self.start_pos+[0,self.width-1+BORDER_OFFSET])
    
    def draw(self, canvas, T, linewidth, delete_command=None):
        if delete_command != None:
            delete_rect = canvas.create_rectangle(T(self.side1[0]),T(self.side2[0]),
                                                  fill="#ffa0a0", activefill="#ff2020")
            self.add_delete_command(canvas, delete_rect, delete_command)
        canvas.create_rectangle(T(self.start_or_finish[0]),T(self.side2[0]),
                                width=linewidth,fill="green" if self.is_start else "red", outline="")
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
        return {"block_style": self.class_name,
                "is_vertical": self.is_vertical,
                "is_left_or_down": self.is_left_or_down,
                "start_pos": tuple(map(int,self.start_pos)),
                "width": self.width,
                "is_start": self.is_start}

    @classmethod
    def from_json(cls, data):
        return StartFinishBlock(is_vertical=data["is_vertical"], is_left_or_down=data["is_left_or_down"], start_pos=np.array(data["start_pos"]), width=data["width"], is_start=data["is_start"])
    
    @classmethod
    def from_orientation(cls, orientation, left_or_down_position, width, is_start):
        """orientation: 0=up, 1=down, 2=left, 3=right;"""
        return StartFinishBlock(orientation <= 1, orientation in {1,2}, left_or_down_position, width, is_start)

    
    def __repr__(self):
        return f"{'Start' if self.is_start else 'Finish'}({['right','left','up','down'][self.is_vertical*2+self.is_left_or_down]},{self.start_pos},{self.width})"

    def __eq__(self, value):
        return (isinstance(value, StartFinishBlock) and
                self.is_vertical == value.is_vertical and
                self.is_left_or_down == value.is_left_or_down and
                np.array_equal(self.start_pos, value.start_pos) and
                self.width == value.width and
                self.is_start == value.is_start)
