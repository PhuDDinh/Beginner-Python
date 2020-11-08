# Take any possible Dict and diplay it like an inventory of items:

items = {"arrow": 12, "gold coin": 42, "rope": 1, "torch": 6, "dagger": 1}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Total number of items: {}".format(item_total))

displayInventory(items)


def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory
        

inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)





    
