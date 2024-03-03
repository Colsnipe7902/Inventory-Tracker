def view_inventory():
    num_items = len(inventory)
    print("--------------------------------------")
    print(f"{num_items} Items in your inventory:")
    pass
print("----------------------------------------")
def display_options():
    options = "(1) View Inventory (2) Add Item (3) Drop Item (4) Exit "
    selected_option = int(input(options))
    return selected_option
inventory = ['shield', 'potion', 'sword', 'bow', 'arrows']

def add_item():
    item = (input ("What item do you want to add."))
    inventory.append (item)
    print(f"{item} added to inventory")

def drop_item():
    view_inventory()
    index = int(input("Enter index of item to drop: "))
    dropped_item = inventory.pop(index)
    print(f"Removed {dropped_item} from inventory")


while True:
    selected_option = display_options()
    if selected_option == 1:
        view_inventory()
    elif selected_option == 2:
        add_item()
    elif selected_option == 3:
        drop_item()
    elif selected_option == 4:
        print("Goodbye!")
        break

