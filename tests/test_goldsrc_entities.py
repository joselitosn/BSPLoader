import unittest
from bspfile import BSPFile


class GoldSrcEntityTest(unittest.TestCase):
    def setUp(self):
        self.bsp = BSPFile('fy_new_pool_day.bsp')

    def test_entities_player_ct(self):
        self.assertEqual(len(self.bsp.entities.get('info_player_start')), 16, 'Incorrect number of CTs spawns.')

    def test_entities_player_t(self):
        self.assertEqual(len(self.bsp.entities.get('info_player_deathmatch')), 16, 'Incorrect number of Ts spawns.')


if __name__ == '__main__':
    unittest.main()
