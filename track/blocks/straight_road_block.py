
from .road_block import RoadBlock

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
        print(self)
        if self.is_vertical:
            print("here")
            canvas.create_line((T(self.left-1/2, self.bottom-1/2)),
                               (T(self.left-1/2, self.top+1/2)),
                               width=linewidth)
            canvas.create_line((T(self.right+1/2, self.bottom-1/2)),
                               (T(self.right+1/2, self.top+1/2)),
                               width=linewidth)
        else:
            canvas.create_line((T(self.left-1/2, self.bottom-1/2)),
                               (T(self.right+1/2, self.bottom-1/2)),
                               width=linewidth)
            canvas.create_line((T(self.left-1/2, self.top+1/2)),
                               (T(self.right+1/2, self.top+1/2)),
                               width=linewidth)

    def list_positions(self):
        """The allowed positions are the whole rectangle"""
        return {(i, j) for i in range(self.left, self.right+1) for j in range(self.bottom, self.top+1)}

    def __repr__(self):
        return f"StraightBlock({'vertical' if self.is_vertical else 'horizontal'}, top:{self.top}, bottom:{self.bottom}, left:{self.left}, right:{self.right})"
