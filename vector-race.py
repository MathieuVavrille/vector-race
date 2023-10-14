
import argparse
import sys,os

sys.path.insert(0,os.path.join(os.path.split(__file__)[0],"src"))

from map_editor.map_editor import MapEditor
from game import Game
from track.track import Track


def get_args():
    parser = argparse.ArgumentParser(description = "Vector Race. A racing game on a grid. And the associated map editor")
    parser.add_argument("-t", "--track", type = str, metavar="track", default = "", help = "Selected track to load")
    parser.add_argument("-e", "--editor", action="store_true", help = "Run the editor or not.")
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    if args.track == "":
        if args.editor:
            track = Track.empty()
        else:
            track = Track.straight_line_vertical(10, 4)
    else:
        track = Track.from_json_file(args.track)
    if args.editor:
        app = MapEditor(track)
    else:
        app = Game(track)
    app.mainloop()
        

if __name__  == "__main__":
    main()
