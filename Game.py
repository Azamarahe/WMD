import Event
import Graphics
import Interface


class Game:
    def __init__(self):
        Interface.Interface(Event.Event(),Graphics.Graphics())
