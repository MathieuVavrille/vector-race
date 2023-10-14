
import numpy as np
import json

from .blocks.road_block import RoadBlock
from .blocks.start_finish_block import StartFinishBlock
from .blocks.straight_road_block import StraightRoadBlock
from .blocks.ellipsis_turn_block import EllipsisTurnBlock

class Track:

    def __init__(self, start_blocks, finish_blocks, blocks):
        self.start_blocks = start_blocks
        self.finish_blocks = finish_blocks
        self.blocks = blocks+start_blocks+finish_blocks
        

    def draw(self, canvas, T, linewidth, allow_delete=None):
        """allow_delete = update_canvas if we allow to delete"""
        for block in self.blocks:
            block.draw(canvas, T, linewidth, delete_command=self.delete_block_event(allow_delete) if allow_delete else None)

    def delete_block_event(self, update_canvas):
        def temp1(block_to_delete):
            def temp2(event):
                print("delete_here")
                self.start_blocks=[block for block in self.start_blocks if block!=block_to_delete]
                self.finish_blocks=[block for block in self.finish_blocks if block!=block_to_delete]
                self.blocks = [block for block in self.blocks if block!=block_to_delete]
                update_canvas()
            return temp2
        return temp1
    
    def get_allowed_positions(self):
        allowed_positions = set()
        for block in self.blocks:
            allowed_positions.update(block.list_positions())
        return allowed_positions

    def add(self, new_block):
        if isinstance(new_block, StartFinishBlock):
            if new_block.is_start:
                self.start_blocks.append(new_block)
            else:
                self.finish_blocks.append(new_block)
        self.blocks.append(new_block)

    def get_start_positions(self):
        start_positions = set()
        for block in self.start_blocks:
            start_positions.update(block.list_positions())
        return start_positions

    def save_to_json(self, filename):
        json_blocks = [block.to_json() for block in self.blocks]
        with open(filename,"w") as f:
            json.dump(json_blocks, f)

    @classmethod
    def from_json_file(cls, filename):
        with open(filename, "r") as f:
            data = json.loads(f.read())
        created_track = Track.empty()
        for json_block in data:
            created_track.add(RoadBlock.parse_block_style_json(json_block))
        return created_track

    @classmethod
    def empty(cls):
        return Track([],[],[])
        
    @classmethod
    def straight_line_vertical(cls, length, width):
        start = StartFinishBlock.from_orientation(0, np.array([0,0]), width, True)
        finish = StartFinishBlock.from_orientation(1, np.array([0,length-1]), width, False)
        return Track([start], [finish], [StraightRoadBlock.from_position(width, length, (0,0), True)])
        
    @classmethod
    def straight_line_horizontal(cls, length, width):
        start = StartFinishBlock.from_orientation(3, np.array([0,0]), length, True)
        finish = StartFinishBlock.from_orientation(2, np.array([width-1,0]), length, False)
        return Track([start], [finish], [StraightRoadBlock.from_position(width, length, (0,0), False)])

    @classmethod
    def one_turn(cls):
        start = StartFinishBlock.from_orientation(0, np.array([0,0]), 4, True)
        finish = StartFinishBlock.from_orientation(1, np.array([7,7]), 2, False)
        return Track([start], [finish], [EllipsisTurnBlock(np.array([6,0]), 90, np.array([3,2]),np.array([6,4])),
                                         EllipsisTurnBlock(np.array([6,7]), 270, np.array([1,3]),np.array([2,5]))])
        

