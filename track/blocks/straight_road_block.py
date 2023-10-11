
import numpy as np

from .road_block import RoadBlock
from constants import BORDER_OFFSET

class StraightRoadBlock(RoadBlock):

    def __init__(self, width, height, bottom_left, is_vertical):
        self.left = bottom_left[0]
        self.right = self.left+width-1
        self.bottom = bottom_left[1]
        self.top = self.bottom+height-1
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

    def __repr__(self):
        return f"StraightBlock({'vertical' if self.is_vertical else 'horizontal'}, top:{self.top}, bottom:{self.bottom}, left:{self.left}, right:{self.right})"
