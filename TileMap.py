from toolkit import *


class Tile:
    def __init__(self):
        pass


class TileMap:
    def __init__(self):
        # todo: viewport may need to be its own class
        self.Viewport = Rect(0, 0, 100, 100)
        self.TileWidth = 10
        self.TileHeight = 10
        self.Tile = [[Tile() for x in range(100)] for y in range(100)]

    def GetTile(self, pos):
        # take cursor position, adjust for viewport location
        x = (pos[0] + self.Viewport.left) // self.TileWidth
        y = pos[1] + self.Viewport.top // self.TileHeight
        #todo: these should be try catch, make wording more specific than standard OOB and instance exceptions
        if x >= len(self.Tile): raise WMDError("Target tile out of x range")
        if x >= len(self.Tile[x]): raise WMDError("Target tile out of y range")
        if not isinstance(self.Tile[x][y], Tile): raise WMDError("Target tile not initialized")
        return self.Tile[x][y]

    def GetTileOptions(self, tile, round_):
        options = []
        # separate lists in case UI functions are moved from tilemap listener to e.g. tools
        #todo: clarify that buildings list is virtual/available
        [options.append(building.CanPlace(tile, round_)) for building in round_.GetBuildings()]
        return options
