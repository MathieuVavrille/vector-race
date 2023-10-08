
from .road_block import RoadBlock

class StraightRoadBlock(RoadBlock):

    def __init__(self, width, height, bottom_left, is_vertical):
        self.left = bottom_left[0]
        self.right = bottom_left[0]+width-1
        self.bottom = bottom_left[1]
        self.top = bottom_left[1]+height-1
        self.is_vertical = is_vertical

    def check(self, x, y):
        return self.left <= x <= self.right and self.bottom <= y <= self.top

    def draw(self, canvas, T):
        print(self)
        if self.is_vertical:
            print("here")
            canvas.create_line((T(self.left-1/2), T(self.bottom-1/2)),
                               (T(self.left-1/2), T(self.top+1/2)))
            canvas.create_line((T(self.right+1/2), T(self.bottom-1/2)),
                               (T(self.right+1/2), T(self.top+1/2)))
        else:
            canvas.create_line((T(self.left-1/2), T(self.bottom-1/2)),
                               (T(self.right+1/2), T(self.bottom-1/2)))
            canvas.create_line((T(self.left-1/2), T(self.top+1/2)),
                               (T(self.right+1/2), T(self.top+1/2)))

    def __repr__(self):
        return f"StraightBlock({'vertical' if self.is_vertical else 'horizontal'}, top:{self.top}, bottom:{self.bottom}, left:{self.left}, right:{self.right})"
