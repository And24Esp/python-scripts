# Done by toonarmycaptain at GitHub
# https://gist.github.com/toonarmycaptain/22d6f14681c4cf11dea2044df54a0861

from collections import Counter

# players current inventory before killing dragon
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# items from the slain dragon
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# this function prints the players inventory in a list and reports the total items
def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
        item_total = item_total + int(v)
    print("\nTotal number of items: " + str(item_total))

# this function adds the dragon's stuff to the players inventory
def add_to_inventory(inventory, added_items):
        added_items_dict ={i:added_items.count(i) for i in added_items}
        inv = Counter(inventory) + Counter(added_items_dict)
        return inv

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
