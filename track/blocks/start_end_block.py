
from .road_block import RoadBlock

class StartEndBlock(RoadBlock):

    def __init__(self, orientation, left_or_up_position, width, is_start):
        """orientation: 0=up, 1=down, 2=left, 3=right;
        start_pos is the position of the start of the block (upmost or leftmost);
        width is the width of the block, should be > 0 (it is the number of starting positions)."""
        self.is_vertical = orientation <= 1
        self.is_left_or_up = orientation%2 == 0
        self.start_pos = left_or_up_position
        self.width = width
        self.is_start = is_start
    
    def check(self, x, y):
        if self.is_vertical:
            return self.start_pos[0]==x and self.start_pos[1] <= y < self.left[1]+self.width
        else:
            return self.start_pos[0] <= x < self.left[0] and self.left[1] == y

    def draw(self, canvas, T):
        print(self)
        if self.is_vertical:
            canvas.create_line(T(self.start_pos[0]-1/2, self.start_pos[1]+1/2),
                               T(self.start_pos[0]-1/2, self.start_pos[1]-1/2))
            canvas.create_line(T(self.start_pos[0]+self.width-1/2, self.start_pos[1]+1/2),
                               T(self.start_pos[0]+self.width-1/2, self.start_pos[1]-1/2))
            canvas.create_line(T(self.start_pos[0]-1/2, self.start_pos[1]),
                               T(self.start_pos[0]+self.width-1/2, self.start_pos[1]),
                               fill="green" if self.is_start else "red")
            side = 1/2 if self.is_left_or_up else -1/2
            canvas.create_line(T(self.start_pos[0]-1/2, self.start_pos[1]-side),
                               T(self.start_pos[0]+self.width-1/2, self.start_pos[1]-side))
        else:
            raise NotImplementedError("TODO")

    def list_positions(self):
        """The positions allowed by the block are on the start/end line"""
        if self.is_vertical:
            return {(self.start_pos[0]+i, self.start_pos[1]) for i in range(width)}
        else:
            return {(self.start_pos[0], self.start_pos[1]-i) for i in range(width)}

    def __repr__(self):
        return f"{'Start' if self.is_start else 'End'}({['right','left','down','up'][self.is_vertical*2+self.is_left_or_up]},{self.start_pos},{self.width})"
