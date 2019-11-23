player_inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

wizard_loot = ['gold coin', 'gold coin', 'bow', 'gold coin', 'emerald', 'invisibility cloak']

def display_inventory(inventory):
	print("Your Inventory has:")
	count = 0
	for k, v in inventory.items():
		print(str(v) + '\t' + k)
		count += v
	print("So you have a total of {} items.\n".format(str(count)))

def add_to_inventory(inventory, items):
	""" (dict, list) -> dict """
	for item in items:
		if item not in inventory.keys():
			inventory[item] = 1
		else:
			inventory[item] += 1

display_inventory(player_inv)
add_to_inventory(player_inv, wizard_loot)
display_inventory(player_inv)