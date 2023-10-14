
import numpy as np

from .road_block import RoadBlock
from constants import BORDER_OFFSET

class StraightRoadBlock(RoadBlock):

    class_name="StraightRoadBlock"

    def __init__(self, left, right, bottom, top, is_vertical, **kwargs):
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top
        self.is_vertical = is_vertical

    def check(self, x, y):
        return self.left <= x <= self.right and self.bottom <= y <= self.top

    def draw(self, canvas, T, linewidth):
        if self.is_vertical:
            canvas.create_line(T(np.array([self.left-BORDER_OFFSET, self.bottom])),
                               T(np.array([self.left-BORDER_OFFSET, self.top])),
                               width=linewidth)
            canvas.create_line(T(np.array([self.right+BORDER_OFFSET, self.bottom])),
                               T(np.array([self.right+BORDER_OFFSET, self.top])),
                               width=linewidth)
        else:
            canvas.create_line(T(np.array([self.left, self.bottom-BORDER_OFFSET])),
                               T(np.array([self.right, self.bottom-BORDER_OFFSET])),
                               width=linewidth)
            canvas.create_line(T(np.array([self.left, self.top+BORDER_OFFSET])),
                               T(np.array([self.right, self.top+BORDER_OFFSET])),
                               width=linewidth)

    def list_positions(self):
        """The allowed positions are the whole rectangle"""
        return {(i, j) for i in range(self.left, self.right+1) for j in range(self.bottom, self.top+1)}

    def to_json(self):
        return {"block_style": self.class_name,
                "left": int(self.left),
                "right": int(self.right),
                "bottom": int(self.bottom),
                "top": int(self.top),
                "is_vertical": self.is_vertical}

    @classmethod
    def from_json(cls, data):
        return StraightRoadBlock(**data)

    @classmethod
    def from_position(cls, width, height, bottom_left, is_vertical):
        return StraightRoadBlock(bottom_left[0], bottom_left[0]+width-1, bottom_left[1], bottom_left[1]+height-1, is_vertical)

    def __repr__(self):
        return f"StraightBlock({'vertical' if self.is_vertical else 'horizontal'}, top:{self.top}, bottom:{self.bottom}, left:{self.left}, right:{self.right})"

    def __eq__(self, value):
        return (isinstance(value, StraightRoadBlock) and
                self.left == value.left and
                self.right == value.right and
                self.bottom == value.bottom and
                self.top == value.top and
                self.is_vertical == value.is_vertical)
                
