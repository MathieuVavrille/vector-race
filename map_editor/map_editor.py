
from tkinter import *
import numpy as np
from random import choice
import os

from track.track import Track
from camera import Camera
from constants import *
from .block_selection import BlockSelection

canvas_size = np.array([500,500])

class MapEditor(Frame):

    def __init__(self, track, master = None):
        """Initialization of all the data"""
        Frame.__init__(self, master)
        self.grid()
        self.track = track
        self.camera = Camera(canvas_size)
        self.bind_all("<Escape>", lambda x:self.quit())
        self.init_canvas()
        self.set_navigation_buttons()
        self.update()
        self.canv.bind("<Motion>", self.motion)
        self.block_selection = BlockSelection(self)
        self.block_selection.grid(column=1, row=0)

        self.previous_mouse_position = None
        self.rotation = 0

        self.save_frame = Frame(self)
        self.save_frame.grid(column=1,row=1)
        self.save_button = Button(self.save_frame, text="Save", command=self.save_track)
        self.save_button.grid(column=0,row=0)
        self.save_main_folder_label = Label(self.save_frame, text="saved_tracks/")
        self.save_main_folder_label.grid(column=1,row=0)
        self.save_filename = Text(self.save_frame, height=1, width=20)
        self.save_filename.insert("1.0","track1")
        self.save_filename.grid(column=2,row=0)
        self.save_main_folder_label = Label(self.save_frame, text=".trk")
        self.save_main_folder_label.grid(column=3,row=0)

    def save_track(self):
        os.makedirs("saved_tracks",exist_ok=True)
        filename = self.save_filename.get('1.0','end').replace("\n", "")
        print(filename)
        self.track.save_to_json(os.path.join("saved_tracks",f"{filename}.trk"))

    def place_block(self, event):
        new_block = self.block_selection.get_block(self.previous_mouse_position, self.rotation)
        self.track.add(new_block)
        
    def increase_rotation(self, event):
        self.rotation += 1
        self.update(added_block=self.block_selection.get_block(self.previous_mouse_position, self.rotation))

    def motion(self, event):
        int_pos = self.camera.invert_transform((event.x, event.y))
        if not np.array_equal(int_pos, self.previous_mouse_position):
            self.previous_mouse_position = int_pos
            self.update(added_block=self.block_selection.get_block(int_pos, self.rotation))
            
    def set_navigation_buttons(self):
        self.navigation_frame = Frame(self, borderwidth = 5, relief="groove")
        self.navigation_frame.grid(column=0, row=1)
        self.zoom_text = Label(self.navigation_frame, text="zoom")
        self.zoom_text.grid(column=0,row=1)
        self.zoomout_button = Button(self.navigation_frame, text="-", command=self.camera.zoom(self.update, 1))
        self.zoomout_button.grid(column=1, row=1)
        self.zoomin_button = Button(self.navigation_frame, text="+", command=self.camera.zoom(self.update, -1))
        self.zoomin_button.grid(column=2, row=1)

        for text,incr,col,row in [("<",[-1,0],3,1),("^",[0,1],4,0),("v",[0,-1],4,2),(">",[1,0],5,1)]:
            Button(self.navigation_frame, text=text, command=self.camera.move(np.array(incr),self.update)).grid(column=col, row=row)

    def init_canvas(self, rowspan=1):
        self.canvas_frame = Frame(self, borderwidth = 10, relief="ridge")
        self.canvas_frame.grid(column=0,row=0,rowspan=rowspan)
        self.canv = Canvas(self.canvas_frame, width=canvas_size[0], height=canvas_size[1],bg="white")
        self.canv.grid()
        self.canv.bind("<Button-1>", self.place_block)
        self.canv.bind("<Button-3>", self.increase_rotation)
    
    def update(self, plot_next_action = True, added_block=None):
        self.canv.delete("all")
        self.track.draw(self.canv, self.camera.transform, self.camera.scale*LINEWIDTH_PROPORTION)
        for allowed_position in self.track.get_allowed_positions():
            canvas_pos = self.camera.transform(np.array(allowed_position))
            self.canv.create_oval(tuple(canvas_pos-self.camera.scale*DOT_PROPORTION), tuple(canvas_pos+self.camera.scale*DOT_PROPORTION), fill="black")
        if added_block != None:
            added_block.draw(self.canv, self.camera.transform, self.camera.scale*LINEWIDTH_PROPORTION)
            for allowed_position in added_block.list_positions():
                canvas_pos = self.camera.transform(np.array(allowed_position))
                self.canv.create_oval(tuple(canvas_pos-self.camera.scale*DOT_PROPORTION), tuple(canvas_pos+self.camera.scale*DOT_PROPORTION), fill="black")
            
