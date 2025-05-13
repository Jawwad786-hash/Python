print("Mohd Jawwad Ali Farooqui,USN:1AY24AI070,SEC:O")
game_inventory = {'rope' : 1, 'gold coin' : 42}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inventory, addedItems):
	print('Inventory:')
	total = 0
	for k, v in inventory.items():
		if k in addedItems:
			o=addedItems.count(k)
			inventory[k]=v+o
	for k2 in addedItems:
		if k2 not in inventory.keys():
			inventory[k2]=addedItems.count(k2)
	for k3, v2 in inventory.items():
		print(v2, k3)
		total += v2
	print('The total no of items is: ' + str(total))
addToInventory(game_inventory, dragon_loot)
