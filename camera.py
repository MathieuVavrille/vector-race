
import numpy as np

BASE_ZOOM = 1/5
SCALE_EXPONENT = 1.5

class Camera:

    def __init__(self, window_size):
        self.pos = np.array([0,0])
        self.scale = 50
        self.scale_zoom = 0
        self.window_size = window_size

    def update(self, player):
        self.pos = player.pos + player.speed/2
        self.scale = min(self.window_size)/max(max(abs(player.speed)),2)*BASE_ZOOM*SCALE_EXPONENT**self.scale_zoom
        
    def transform(self, x, y, offset=np.array([0,0])):
        coord = np.array([x,y])
        return tuple(self.scale*(coord-self.pos)+self.window_size/2+offset)


        
