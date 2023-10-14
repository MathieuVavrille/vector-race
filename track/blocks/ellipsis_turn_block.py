
import numpy as np

from .road_block import RoadBlock
from constants import BORDER_OFFSET

def ellipsis_value(pos, center, radius):
    return (pos[0]-center[0])**2/radius[0]**2 + (pos[1]-center[1])**2/radius[1]**2
                           
class EllipsisTurnBlock(RoadBlock):

    class_name = "EllipsisTurnBlock"

    def __init__(self, center, angle, inside_rad, outside_rad):
        self.center = center
        self.angle = angle
        self.inside_rad = inside_rad
        self.outside_rad = outside_rad
        
    def draw(self, canvas, T, linewidth, delete_command=None):
        if delete_command != None:
            delete_arc = canvas.create_arc(T(self.center-self.outside_rad-BORDER_OFFSET),
                                           T(self.center+self.outside_rad+BORDER_OFFSET),
                                           start=self.angle,extent=90,style="pieslice",
                                           fill="#ffa0a0", activefill="#ff2020", outline="red")
            self.add_delete_command(canvas, delete_arc, delete_command)
        canvas.create_arc(T(self.center-self.inside_rad+BORDER_OFFSET),
                          T(self.center+self.inside_rad-BORDER_OFFSET),
                          start=self.angle, extent=90, width=linewidth, style="arc")
        canvas.create_arc(T(self.center-self.outside_rad-BORDER_OFFSET),
                          T(self.center+self.outside_rad+BORDER_OFFSET),
                          start=self.angle, extent=90, width=linewidth, style="arc")

    def list_positions(self):
        """Lists all the positions allowed by this block as a of pairs (tuples)."""
        if self.angle in {0, 270}:
            range_x = range(self.center[0], self.center[0]+self.outside_rad[0]+1)
        else:
            range_x = range(self.center[0]-self.outside_rad[0], self.center[0]+1)
        if self.angle in {0,90}:
            range_y = range(self.center[1], self.center[1]+self.outside_rad[1]+1)
        else:
            range_y = range(self.center[1]-self.outside_rad[1], self.center[1]+1)
        allowed = set()
        for x in range_x:
            for y in range_y:
                if ellipsis_value(np.array([x,y]), self.center, self.outside_rad+BORDER_OFFSET) <= 1 and ellipsis_value(np.array([x,y]), self.center, self.inside_rad-BORDER_OFFSET) >= 1:
                    allowed.add((x,y))
        return allowed

    def to_json(self):
        return {"block_style": self.class_name,
                "center": tuple(map(int,self.center)),
                "angle": self.angle,
                "inside_rad": tuple(map(int,self.inside_rad)),
                "outside_rad": tuple(map(int,self.outside_rad))}

    def __eq__(self, value):
        return (isinstance(value, EllipsisTurnBlock) and
                np.array_equal(self.center, value.center) and
                self.angle == value.angle and
                np.array_equal(self.inside_rad, value.inside_rad) and
                np.array_equal(self.outside_rad, value.outside_rad))
            

    @classmethod
    def from_json(cls, data):
        return StraightRoadBlock(np.array(data["center"]),
                                 data["angle"],
                                 np.array(data["inside_rad"]),
                                 np.array(data["outside_rad"]))
    
    def __repr__(self):
        return f"EllipsisTurn({tuple(self.center)}, {tuple(self.inside_rad)}, {tuple(self.outside_rad)})"

 
