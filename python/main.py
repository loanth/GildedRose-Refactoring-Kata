from gilded_rose import Item, GildedRose

if __name__ == '__main__':
    items = [Item("Aged Brie", 1, 0)]
    gilded_rose = GildedRose(items)
    for _ in range(50):
        gilded_rose.update_quality()
        print(items[0])