
from road_block import RoadBlock

class StraightRoadBlock(RoadBlock):

    def __init__(self, width, height, bottom_left, is_vertical):
        self.left = bottom_left[0]
        self.right = bottom_left[0]+width-1
        self.bottom = bottom_left[1]
        self.top = bottom_left[1]+length-1
        self.is_vertical = is_vertical

    def check(self, x, y):
        return self.left <= x <= self.right and self.bottom <= y <= self.top

    def draw(self, canvas, transform):
        if self.is_vertical:
            canvas.draw_line((transform(self.left-1/2), transform(self.bottom)),
                            (transform(self.left-1/2), transform(self.top)))
            canvas.draw_line((transform(self.right+1/2), transform(self.bottom)),
                            (transform(self.right+1/2), transform(self.top)))
        else:
            canvas.draw_line((transform(self.left), transform(self.bottom-1/2)),
                             (transform(self.right), transform(self.bottom-1/2)))
            canvas.draw_line((transform(self.left), transform(self.top+1/2)),
                             (transform(self.right), transform(self.top+1/2)))
            
