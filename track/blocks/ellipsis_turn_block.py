
import numpy as np

from .road_block import RoadBlock
from constants import BORDER_OFFSET

def ellipsis_value(pos, center, radius):
    return (pos[0]-center[0])**2/radius[0]**2 + (pos[1]-center[1])**2/radius[1]**2
                           
class EllipsisTurnBlock(RoadBlock):

    def __init__(self, center, angle, inside_rad, outside_rad):
        self.center = center
        self.angle = angle
        self.inside_rad = inside_rad
        self.outside_rad = outside_rad
        #self.inside_offset = np.array({0:[-1,-1],90:[1,-1],180:[1,1],270:[-1,1]}[self.angle])
        
    def check(self, x, y):
        raise NotImplementedError("TODO ?")

    def draw(self, canvas, T, linewidth):
        """canvas.create_arc(T(self.center-self.inside_rad+self.inside_offset),
                          T(self.center+self.inside_rad+self.inside_offset),
                          start=self.angle, extent=90, width=linewidth, style="arc")
        canvas.create_arc(T(self.center-self.outside_rad+self.inside_offset-1),
                          T(self.center+self.outside_rad+self.inside_offset+1),
                          start=self.angle, extent=90, width=linewidth, style="arc")"""
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
    #raise NotImplementedError("TODO")

    def __repr__(self):
        return f"EllipsisTurn({tuple(self.center)}, {tuple(self.inside_rad)}, {tuple(self.outside_rad)})"

 
