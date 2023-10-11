
from tkinter import *
import numpy as np
from random import choice

from track.track import Track
from camera import Camera
from constants import *

canvas_size = np.array([500,500])

class Application(Frame):

    def __init__(self, track, master = None):
        """Initialization of all the data"""
        Frame.__init__(self, master)
        self.grid()
        self.init_canvas()
        self.track = track
        self.bind_all("<Escape>", lambda x:self.quit())
        self.camera = Camera(canvas_size)
        self.set_navigation_buttons()
        self.update()

    def set_navigation_buttons(self):
        self.navigation_frame = Frame(self, borderwidth = 5, relief="groove")
        self.navigation_frame.grid(column=0, row=1)
        self.zoom_text = Label(self.navigation_frame, text="zoom")
        self.zoom_text.grid(column=0,row=0)
        self.zoomout_button = Button(self.navigation_frame, text="-", command=self.camera.zoom(self.update, 1))
        self.zoomout_button.grid(column=1, row=0)
        self.zoomin_button = Button(self.navigation_frame, text="+", command=self.camera.zoom(self.update, -1))
        self.zoomin_button.grid(column=2, row=0)

    def init_canvas(self, rowspan=1):
        self.canvas_frame = Frame(self, borderwidth = 10, relief="ridge")
        self.canvas_frame.grid(column=0,row=0,rowspan=rowspan)
        self.canv = Canvas(self.canvas_frame, width=canvas_size[0], height=canvas_size[1],bg="white")
        self.canv.grid()
    
    def update(self, plot_next_action = True):
        self.canv.delete("all")
        self.track.draw(self.canv, self.camera.transform, self.camera.scale*LINEWIDTH_PROPORTION)
        for allowed_position in self.track.get_allowed_positions():
            canvas_pos = self.camera.transform(np.array(allowed_position))
            self.canv.create_oval(tuple(canvas_pos-np.array([self.camera.scale,self.camera.scale])*DOT_PROPORTION), tuple(canvas_pos+np.array([self.camera.scale, self.camera.scale])*DOT_PROPORTION), fill="black")
            

if __name__ == "__main__":
    app = Application(Track.one_turn())
    app.mainloop()
