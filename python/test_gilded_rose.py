# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_brie_nom(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Aged Brie", items[0].name)

    def test_brie_sellin_pos(self):
        items = [Item("Aged Brie", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_brie_sellin_neg(self):
        items = [Item("Aged Brie", -1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_brie_quality_50(self):
        items = [Item("Aged Brie", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
