

class RoadBlock:

    def draw(self, canvas, transform):
        """Draws the road block on the canvas. A transformation is applied to scale and offset the drawing."""
        raise NotImplementedError("draw: RoadBlocks is abstract, use other definitions of roads blocks")

    def list_positions(self):
        """Lists all the positions allowed by this block as a set."""
        raise NotImplementedError("list_positions: RoadBlocks is abstract, use other definitions of roads blocks")

    def to_json(self):
        """Returns a dictionnary that can then be reloaded later"""
        raise NotImplementedError("to_json: RoadBlocks is abstract, use other definitions of roads blocks")

    def add_delete_command(self, canvas, delete_id, delete_command):
        canvas.tag_bind(delete_id, "<Button-1>", delete_command(self))

    @classmethod
    def parse_block_style_json(cls, data):
        from .start_finish_block import StartFinishBlock
        from .straight_road_block import StraightRoadBlock
        from .ellipsis_turn_block import EllipsisTurnBlock
        if data["block_style"] == StartFinishBlock.class_name:
            return StartFinishBlock.from_json(data)
        elif data["block_style"] == StraightRoadBlock.class_name:
            return StraightRoadBlock.from_json(data)
        elif data["block_style"] == EllipsisTurnBlock.class_name:
            return EllipsisTurnBlock.from_json(data)
        else:
            raise ValueError("Block not recognized")

    @classmethod
    def from_json(cls, data):
        """Returns the block instantiated from the data"""
        raise NotImplementedError("from_json: RoadBlocks is abstract, use other definitions of roads blocks")
        
        
 
