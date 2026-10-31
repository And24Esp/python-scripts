# Done by toonarmycaptain at GitHub
# https://gist.github.com/toonarmycaptain/22d6f14681c4cf11dea2044df54a0861

print('Exercise 1 inventory:')

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

#def displayInventory(inventory):
#    total_items = 0
#    for item in inventory:
#        print(str(inventory[item])+' '+item)
#        total_items += inventory[item]
#    print("Total number of items: "+str(total_items))
# This worked but I like the following better:

def displayInventory(inventory):
    total_items = 0
    for item, quantity in inventory.items():
        print(str(quantity)+' '+item)
        total_items += quantity
    print("Total number of items: "+str(total_items))

displayInventory(stuff)

print()
print('Exercise 2 inventory:')

inv = {'gold coin': 42, 'rope': 1}
displayInventory(inv)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0) #this adds a (defaulted to zero value) key to the inventory dict if it's not already there
        inventory[item] += 1 #and this increases that value by one, each time that item appears in the loot list
    return inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
