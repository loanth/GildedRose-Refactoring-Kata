from gilded_rose import Item, GildedRose

if __name__ == '__main__':
    items = [Item("Conjured Mana Cake", quality=10, sell_in=10)]
    gilded_rose = GildedRose(items)
    for _ in range(50):
        gilded_rose.update_quality2()
        print(items[0])