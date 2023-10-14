
import numpy as np

from constants import *

class Player:

    def __init__(self,pos=np.array([0,0]), speed=np.array([0,0])):
        self.pos = pos
        self.speed = speed
        self.previous_positions = [self.pos.copy()]

    def draw(self, canvas, camera, plot_next_action=None):
        if len(self.previous_positions) >= 2:
            canvas.create_line(*map(lambda x:tuple(camera.transform(x)), self.previous_positions),fill="#ff10ff", width=camera.scale*LINEWIDTH_PROPORTION, smooth="bezier")
        # Draw player
        canvas.create_oval(tuple(camera.transform(self.pos)-camera.scale*DOT_PROPORTION*PLAYER_DOT_SCALING), tuple(camera.transform(self.pos)+camera.scale*DOT_PROPORTION*PLAYER_DOT_SCALING),fill="blue", outline="")
        if plot_next_action != None:
            for pos, function in self.next_positions():
                canvas_pos = camera.transform(pos)
                dot = canvas.create_oval(tuple(canvas_pos-camera.scale*DOT_PROPORTION*INTERESTING_DOT_SCALING), tuple(canvas_pos+camera.scale*DOT_PROPORTION*INTERESTING_DOT_SCALING), fill="red", activefill="#ff5050", outline="")
                canvas.tag_bind(dot, "<Button-1>", function(*plot_next_action))
            

    def next_positions(self): # warning, does not check edge crossing
        next_center = self.pos+self.speed
        next_positions = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                new_pos = next_center+[i,j]
                next_positions.append((new_pos,self.update_position(np.array([i,j]))))
        return next_positions
                    
    def update_position(self, difference):
        def callback(track, update_callback, error_callback, win_callback):
            def temp(event=None):
                self.speed += difference
                is_error = False #test here if goes outside with segments
                self.pos += self.speed
                self.previous_positions.append(self.pos.copy())
                is_error = tuple(self.pos) not in track.get_all_allowed_positions() # TODO intersection
                is_win = tuple(self.pos) in track.get_finish_positions()
                update_callback(plot_next_action=not (is_error or is_win))
                if is_error:
                    error_callback()
                if is_win:
                    win_callback()
            return temp
        return callback
    
