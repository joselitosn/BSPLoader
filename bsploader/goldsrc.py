from collections import UserDict, UserList
from struct import unpack


class GoldSrcBSP(object):
    version = 30
    LUMPS = (
        'ENTITIES', 'PLANES', 'TEXTURES', 'VERTICES', 'VISIBILITY', 'NODES', 'TEXINFO', 'FACES', 'LIGHTING',
        'CLIPNODES', 'LEAVES', 'MARKSURFACES', 'EDGES', 'SURFEDGES', 'MODELS')

    def __init__(self, filename):
        with open(filename, 'rb') as file:
            self.lumps = self.BSPLumps(file)

            self.entities = self.BSPEntities(self.read_lump(file, 'ENTITIES').decode('UTF-8'))
            self.textures = self.BSPTextures(self.read_lump(file, 'TEXTURES'))

    def read_lump(self, file, lump_name):
        file.seek(self.lumps[lump_name]['OFFSET'])
        return file.read(self.lumps[lump_name]['SIZE'])

    class BSPLumps(UserDict):
        def __init__(self, file):
            super(GoldSrcBSP.BSPLumps, self).__init__()

            file.seek(4)
            for i in range(len(GoldSrcBSP.LUMPS)):
                lump = unpack('=ii', file.read(8))
                self.data[GoldSrcBSP.LUMPS[i]] = {'OFFSET': lump[0], 'SIZE': lump[1]}

    class BSPEntities(UserDict):
        def __init__(self, data):
            super(GoldSrcBSP.BSPEntities, self).__init__()
            self.parse_entities(data)

        def parse_entities(self, data):
            end = 0

            try:
                while True:
                    start = data.index('{', end)
                    end = data.index('}', start)
                    class_name, entity = self.parse_pairs(data[start: end])

                    if not class_name:
                        continue

                    if class_name in self.data.keys():
                        self.data[class_name].append(entity)
                    else:
                        self.data[class_name] = [entity]
            except ValueError:
                pass

        @staticmethod
        def parse_pairs(data):
            class_name = None
            pairs = {}
            end = 0
            try:
                while True:
                    start = data.index('"', end)
                    end = data.index('\n', start)
                    pair = data[data.index('"', start) + 1:data.rindex('"', start, end)].split('" "')
                    if 'classname' in pair[0]:
                        class_name = pair[1]
                    else:
                        pairs[pair[0]] = pair[1]
            except ValueError:
                pass

            return class_name, pairs

    class BSPTextures(UserList):
        def __init__(self, data):
            super(GoldSrcBSP.BSPTextures, self).__init__()
            self.textures = []
            self.size = unpack('=I', data[0:4])[0]
            textures_offsets = self.get_textures_offsets(data)
            self.get_textures_mipmaps(data, textures_offsets)

        def get_textures_offsets(self, data):
            textures_offsets = []

            for i in range(self.size):
                textures_offsets.append(unpack('=i', data[4 * i: 4 * (i + 1)])[0])

            return textures_offsets

        def get_textures_mipmaps(self, data, offsets):
            for i in range(self.size):
                texture_name = unpack('=16s', data[offsets[i]:offsets[i] + 16])[0].split(b'\x00')[0]
