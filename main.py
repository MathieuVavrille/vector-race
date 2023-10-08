from tkinter import *

from track.track import Track

def linear_transform(scale, origin):
    def T(v):
        s = scale*(v-origin)
        print(v,s)
        return s
    return T

WIDTH = 500
BORDERWIDTH = WIDTH//100

class Application(Frame):

    def __init__(self, track, size=WIDTH, master = None):
        """Initialization of all the data"""
        Frame.__init__(self, master)
        self.track = track
        self.grid()
        self.bind_all("<Escape>", lambda x:self.quit())
        self.canv = Canvas(self, height = size, width = size, relief="ridge", borderwidth = BORDERWIDTH,bg="white")
        self.canv.grid()
        self.update()
    
    def update(self):
        print("update")
        self.track.draw(self.canv, linear_transform(25, -1))
        print("updated")

if __name__ == "__main__":
    app = Application(Track.straight_line(10, 4))
    app.mainloop()
