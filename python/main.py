from gilded_rose import Item, GildedRose

if __name__ == '__main__':
    items = [Item("Backstage passes to a TAFKAL80ETC concert", -12, 0)]
    gilded_rose = GildedRose(items)
    for _ in range(50):
        gilded_rose.update_quality2()
        print(items[0])