
import numpy as np

class Player:

    def __init__(self,pos=np.array([0,0]), speed=np.array([0,0])):
        self.pos = pos
        self.speed = speed

    def next_positions(self): # warning, does not check edge crossing
        next_center = self.pos+self.speed
        next_positions = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                new_pos = next_center+[i,j]
                next_positions.append((new_pos,self.update_position(np.array([i,j]))))
        return next_positions
                    
    def update_position(self, difference):
        def callback(track, update_callback, error_callback):
            def temp(event=None):
                self.speed += difference
                self.pos += self.speed
                is_error = False#tuple(self.pos) not in track.get_allowed_positions() # TODO intersection
                update_callback(plot_next_action=not is_error)
                if is_error:
                    error_callback()
            return temp
        return callback
    
