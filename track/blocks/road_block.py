
from .start_finish_block import StartFinishBlock
from .straight_road_block import StraightRoadBlock
from .ellipsis_turn_block import EllipsisTurnBlock

class RoadBlock:

    def check(self, x, y):
        """Checks whether the position (x,y) is in the RoadBlock."""
        raise NotImplementedError("check: RoadBlocks is abstract, use other definitions of roads blocks")

    def draw(self, canvas, transform):
        """Draws the road block on the canvas. A transformation is applied to scale and offset the drawing."""
        raise NotImplementedError("draw: RoadBlocks is abstract, use other definitions of roads blocks")

    def list_positions(self):
        """Lists all the positions allowed by this block as a set."""
        raise NotImplementedError("list_positions: RoadBlocks is abstract, use other definitions of roads blocks")

    def to_json(self):
        """Returns a dictionnary that can then be reloaded later"""
        raise NotImplementedError("to_json: RoadBlocks is abstract, use other definitions of roads blocks")

    @classmethod
    def parse_block_style_json(cls, data):
        if data["block_style"] == "StartFinishBlock":
            return StartFinishBlock.from_json(data)
        elif data["block_style"] == "StraightRoadBlock":
            return StraightRoadBlock.from_json(data)
        elif data["block_style"] == "EllipsisTurnBlock":
            return EllipsisTurnBlock.from_json(data)
        else:
            raise ValueError("Block not recognized")

    @classmethod
    def from_json(self, data):
        """Returns the block instantiated from the data"""
        raise NotImplementedError("from_json: RoadBlocks is abstract, use other definitions of roads blocks")
        
        
 
