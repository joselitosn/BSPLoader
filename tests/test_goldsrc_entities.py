import unittest
from bsploader import BSP


class GoldSrcBSPEntityTest(unittest.TestCase):
    def setUp(self):
        self.bsp = BSP('aim_galil-famas.goldsrc')

    def test_entities_player_ct(self):
        self.assertEqual(len(self.bsp.entities.get('info_player_start')), 18, 'Incorrect number of CTs spawns.')

    def test_entities_player_t(self):
        self.assertEqual(len(self.bsp.entities.get('info_player_deathmatch')), 18, 'Incorrect number of Ts spawns.')


if __name__ == '__main__':
    unittest.main()
