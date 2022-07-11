from pynput import *

def get_choords(x, y):
    print("Now at: {}".format((x, y)))

with mouse.Listener(on_move = get_choords) as listen:
    listen.join()
