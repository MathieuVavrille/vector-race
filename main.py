
from tkinter import *
import numpy as np
import random

from track.track import Track
from camera import Camera
from player import Player
from constants import *
from map_editor.map_editor import MapEditor

canvas_size = np.array([500,500])

class Application(Frame):

    def __init__(self, track, master = None):
        """Initialization of all the data"""
        Frame.__init__(self, master)
        self.grid()
        self.init_canvas()
        self.track = track
        self.bind_all("<Escape>", lambda x:self.quit())
        self.init_player()
        self.camera = Camera(canvas_size)
        self.update()

    def init_canvas(self):
        self.canvas_frame = Frame(self, borderwidth = 10)
        self.canvas_frame.grid()
        self.canv = Canvas(self.canvas_frame, width=canvas_size[0], height=canvas_size[1],bg="white")
        self.canv.grid()

    def init_player(self):
        self.player = Player(pos=np.array(random.choice(self.track.start_positions)))
    
    def update(self, plot_next_action = True):
        self.camera.update_from_player(self.player)
        self.canv.delete("all")
        self.track.draw(self.canv, self.camera.transform, self.camera.scale*LINEWIDTH_PROPORTION)
        for allowed_position in self.track.get_allowed_positions():
            canvas_pos = self.camera.transform(np.array(allowed_position))
            self.canv.create_oval(tuple(canvas_pos-np.array([self.camera.scale,self.camera.scale])*DOT_PROPORTION), tuple(canvas_pos+np.array([self.camera.scale, self.camera.scale])*DOT_PROPORTION), fill="black")
        # Draw player
        self.canv.create_oval(tuple(self.camera.transform(self.player.pos)-self.camera.scale*DOT_PROPORTION*PLAYER_DOT_SCALING), tuple(self.camera.transform(self.player.pos)+self.camera.scale*DOT_PROPORTION*PLAYER_DOT_SCALING),fill="blue", outline="")
        if plot_next_action:
            for pos, function in self.player.next_positions():
                canvas_pos = self.camera.transform(pos)
                dot = self.canv.create_oval(tuple(canvas_pos-self.camera.scale*DOT_PROPORTION*INTERESTING_DOT_SCALING), tuple(canvas_pos+self.camera.scale*DOT_PROPORTION*INTERESTING_DOT_SCALING), fill="red", activefill="#ff5050", outline="")
                self.canv.tag_bind(dot, "<Button-1>", function(self.track, self.update, lambda:self.after(1000,self.quit)))
            

if __name__ == "__main__":
    app = MapEditor(Track.one_turn())
    app.mainloop()
