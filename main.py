
from tkinter import *
import numpy as np

from track.track import Track
from camera import Camera
from player import Player

canvas_size = np.array([500,500])

class Application(Frame):

    def __init__(self, track, master = None):
        """Initialization of all the data"""
        Frame.__init__(self, master)
        self.grid()
        self.init_canvas()
        self.track = track
        self.bind_all("<Escape>", lambda x:self.quit())
        self.player = Player()
        self.camera = Camera(canvas_size)
        self.camera.update(self.player)
        self.update()

    def init_canvas(self):
        self.canvas_frame = Frame(self, borderwidth = 10)
        self.canvas_frame.grid()
        self.canv = Canvas(self.canvas_frame, width=canvas_size[0], height=canvas_size[1],bg="white")
        self.canv.grid()
    
    def update(self):
        self.canv.delete("all")
        self.track.draw(self.canv, self.camera.transform)
        for x,y in self.track.list_positions():
            self.canv.create_circle(TODO)

if __name__ == "__main__":
    app = Application(Track.straight_line(10, 4))
    app.mainloop()
