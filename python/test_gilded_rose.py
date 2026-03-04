# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

#Test pour le brie
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

#Test pour le sulfuras
    def test_sulfura_nom(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)

    def test_sulfura_sellin_pos(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfura_sellin_neg(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfura_quality_50(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)


#Test pour le Backstage
    def test_backstage_nom(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)

    def test_backstage_sellin_pos(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 16, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(15, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage_sellin_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(22, items[0].quality)

    def test_backstage_sellin_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

    def test_backstage_sellin_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

#Test pour le Conjured
    def test_conjured_nom(self):
        items = [Item("Conjured Mana Cake", 12, 17)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Conjured Mana Cake", items[0].name)

    def test_conjured_sellin_pos(self):
        items = [Item("Conjured Mana Cake", 12, 17)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(15, items[0].quality)

    def test_conjured_sellin_0(self):
        items = [Item("Conjured Mana Cake", 0, 17)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(15, items[0].quality)

    def test_conjured_quality_0(self):
        items = [Item("Conjured Mana Cake", 12, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality2()
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


        
if __name__ == '__main__':
    unittest.main()
