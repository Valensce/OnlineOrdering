import json, os, sys
from cmath import nan
from tkinter import Y

with open(os.path.join(sys.path[0], "customerMenu.json")) as file:
	customerMenu = json.loads(file.read())
	file.close()

ordered = False

def cancel():

	input("\n\nOrder cancelled!\n\nPress Enter to finish.")
	sys.exit()

def orderList():

	selection1_valid = False
	while not selection1_valid:
		selection1 = input("\nEnter item type:\n\n>")
		if selection1 == "cancel":
			cancel()
		mealsInType = []
		for row in customerMenu:
			if selection1 == row["type"]:
				mealsInType.append(row["name"])
				selection1_valid = True

	print(f"\nFound: {mealsInType}\n")

	selection2_valid = False
	while not selection2_valid:
		selection2 = input("\nSelect an item:\n\n")
		if selection2 == "cancel":
			cancel()
		for row in customerMenu:
			if selection2 == row["name"] and selection1 == row["type"]:
				selection2_valid = True
				order = {
					"type": row["type"],
					"name": row["name"]
				}
				break

	print(f"\n\nOrder found: {order}\n")

	confirmation = " "
	while confirmation[0] not in ["y", "n"]:
		confirmation = input("\nConfirm order? [y/n]\n\n>") + " "
		if confirmation == "cancel":
			cancel()
	if confirmation.lower().startswith("y"):
		global ordered
		ordered = True
		global totalOrder
		totalOrder = order
		input(f"\n\nOrder success! {totalOrder}\n\nPress Enter to finish.")
	if confirmation.lower().startswith("n"):
		print("\n\nOrder discarded.\n")

print("\nType \"cancel\" to cancel at any time.")

while ordered == False:
	orderList()

# Result is `totalOrder`
