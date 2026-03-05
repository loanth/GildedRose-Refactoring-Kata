# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self._update_aged_brie(item)
                
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_passes(item)
               
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            elif item.name == "Conjured Mana Cake":
                self._update_conjured(item)
               
            else:
                self._update_other_items(item)

    def _update_aged_brie(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 0:
                if item.quality < 50:
                    item.quality += 1

    def _update_backstage_passes(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 10:
                if item.quality < 50:
                    item.quality += 1
            if item.sell_in < 5:
                if item.quality < 50:
                    item.quality += 1
            if item.sell_in < 0:
                item.quality = 0
        else:
            item.quality = 0

    def _update_conjured(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            if item.quality == 1:
                item.quality = 0
            else:
                item.quality -= 2
        elif item.sell_in < 0:
            if item.quality > 0:
                item.quality -= 2

    def _update_other_items(self, item):
        if item.quality > 0:
            item.quality -= 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
                if item.sell_in < 0:
                    if item.quality > 0:
                        item.quality -= 1
        else:
            item.sell_in -= 1
            
            



    #def update_quality2(self):
     #    for item in self.items:
      #       if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
       #          if item.quality > 0:
        #             if item.name != "Sulfuras, Hand of Ragnaros":
         #                item.quality = item.quality - 1
          #   else:
           #      if item.quality < 50:
            #         item.quality = item.quality + 1
             #        if item.name == "Backstage passes to a TAFKAL80ETC concert":
              #           if item.sell_in < 11:
               #              if item.quality < 50:
                #                 item.quality = item.quality + 1
                 #        if item.sell_in < 6:
                  #           if item.quality < 50:
                   #              item.quality = item.quality + 1
            # if item.name != "Sulfuras, Hand of Ragnaros":
             #    item.sell_in = item.sell_in - 1
             #if item.sell_in < 0:
              #   if item.name != "Aged Brie":
               #      if item.name != "Backstage passes to a TAFKAL80ETC concert":
                #         if item.quality > 0:
                 #            if item.name != "Sulfuras, Hand of Ragnaros":
                  #               item.quality = item.quality - 1
                   #  else:
                    #     item.quality = item.quality - item.quality
                 #else:
                  #   if item.quality < 50:
                   #      item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
