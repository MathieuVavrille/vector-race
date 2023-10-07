
from road_block import RoadBlock

class StartBlock(RoadBlock):

    def __init__(self, orientation, left, width):
        """orientation: 0=up, 1=down, 2=left, 3=right;
        left is the left side of the start, when trying to start the race;
        width is the width of the start, should be > 0 (it is the number of starting positions)."""
        self.orientation = orientation # 0=up, 1=down, 2=left, 3=right
        self.left = left
        self.width = width
    
    def check(self, x, y):
        if self.orientation == 0: # up
            return self.left[0] <= x < self.left[0]+self.width and self.left[1] == y
        elif self.orientation == 1: # down
            return self.left[0]-width < x <= self.left[0] and self.left[1] == y
        elif self.orientation == 2: # up
            return self.left[1] <= x < self.left[1]+self.width and self.left[0] == y
        else self.orientation == 3: # down
            return self.left[1]-width < x <= self.left[1] and self.left[0] == y

    def draw(self, canvas, transform):
        if self.orientation == 0: # up
            canvas.create_line((transform(self.left[0]-1/2), transform(self.left[1]+1/2)),
                               (transform(self.left[0]+1/2), transform(self.left[1]+1/2)))
            canvas.create_line((transform(self.left[0]-1/2), transform(self.left[1]+width1/2)),
                               (transform(self.left[0]+1/2), transform(self.left[1]+1/2)))
            todo
        elif self.orientation == 1: # down
            todo
        elif self.orientation == 2: # left
            todo
        else: # right
            todo
