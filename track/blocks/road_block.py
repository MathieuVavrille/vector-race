
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
 
