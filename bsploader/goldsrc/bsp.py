from enum import Enum, auto


class BSP:
    version = 30

    def __init__(self, fp):
        self.lumps = ''


class Lumps(Enum):
    ENTITIES = 0
    PLANES = auto()
    TEXTURES = auto()
    VERTICES = auto()
    VISIBILITY = auto()
    NODES = auto()
    TEXINFO = auto()
    FACES = auto()
    LIGHTING = auto()
    CLIPNODES = auto()
    LEAVES = auto()
    MARKSURFACES = auto()
    EDGES = auto()
    SURFEDGES = auto()
    MODELS = auto()

    def readlumps(self, fp):
        pass
