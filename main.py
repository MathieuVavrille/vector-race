from tkinter import *



WIDTH = 500
BORDERWIDTH = WIDTH//100

class Application(Frame):

    def __init__(self, size=WIDTH, master = None):
        """Initialization of all the data"""
        Frame.__init__(self, master)
        self.grid()
        self.bind_all("<Escape>", lambda x:self.quit())
        self.canv = Canvas(self, height = size, width = size, relief="ridge", borderwidth = BORDERWIDTH,bg="white")
        self.canv.grid()
    
    


if __name__ == "__main__":
    app = Application()
    app.mainloop()
