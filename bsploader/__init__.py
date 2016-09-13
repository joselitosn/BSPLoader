from struct import unpack

from .goldsrc import GoldSrcBSP


class BSP(object):
    def __new__(cls, filename):
        with open(filename, 'rb') as file:
            file.seek(0)
            version = unpack('=i', file.read(4))[0]

        if version == 30:
            return GoldSrcBSP(filename)
