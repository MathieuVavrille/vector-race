
from roadblock import *

class Track:

    def __init__(self, start_positions, end_positions, road_blocks):
        self.start_positions = start_positions
        self.end_positions = end_positions
        self.road_blocks = road_blocks

    @classmethod
    def straight_line(length, width):
        return Track(
