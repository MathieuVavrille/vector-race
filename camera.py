
import numpy as np
import math

BASE_ZOOM = 1/10
SCALE_EXPONENT = 1.5

class Camera:

    def __init__(self, window_size):
        self.window_size = window_size
        self.pos = np.array([0,0])
        self.scale_zoom = 0
        self.update_scale()

    def update_from_player(self, player):
        self.pos = player.pos + player.speed
        self.scale = min(self.window_size)/max(max(abs(player.speed)),2)*BASE_ZOOM*SCALE_EXPONENT**self.scale_zoom

    def update_scale(self):
        self.scale = min(self.window_size)*BASE_ZOOM*SCALE_EXPONENT**self.scale_zoom
        
    def transform(self, coord, offset=0):
        return tuple((self.scale*(coord-self.pos)
                      +self.window_size/2+offset)
                     *[1,-1]
                     +[0,self.window_size[1]])

    def invert_transform(self, coord, offset=0):
        coord = np.array(coord)
        return np.rint(
            ((coord-[0,self.window_size[1]])
             *[1,-1]
             -self.window_size/2-offset)
            /self.scale
            +self.pos
        ).astype(int)

    def zoom(self, update_canvas, increment=1):
        def temp():
            self.scale_zoom -= increment
            self.update_scale()
            update_canvas()
        return temp

    def move(self, vector, update_canvas):
        def temp():
            print(1/SCALE_EXPONENT**self.scale_zoom)
            exp = max(1,int(1/SCALE_EXPONENT**self.scale_zoom))
            print(exp)
            v = vector*exp
            print(v)
            self.pos += v
            update_canvas()
        return temp
        


        
