# Initialize List 
validItems = ["Water", "Knife", "Matches", "Shelter Materials", "First Aid Kit", "Food", "Compass", "Walkie Talkie", "Map", "Money"]



def is_valid_item(item):
    """
    Check if the item is a valid choice.

    Parameters:
    - item (str): The item to be checked.

    Returns:
    - bool: True if the item is valid, False otherwise.
    """
    return item in validItems


def remove_item(backpack, index):
    """
    Remove an item from the backpack at the specified index.

    Parameters:
    - backpack (list): The list representing the user's backpack.
    - index (int): The index of the item to be removed.

    Returns:
    - tuple: A tuple containing the removed item and the updated backpack.
    """
    if 0 <= index < len(backpack):
        removed_item = backpack.pop(index)
        return removed_item, backpack
    else:
        return None, backpack

def add_item(backpack, item):
    """
    Add an item to the user's backpack.

    Parameters:
    - backpack (list): The list representing the user's backpack.
    - item (str): The item to be added to the backpack.

    Returns:
    - list: The updated backpack.
    """
    backpack.append(item)
    return backpack

def check_combinations(backpack):
    """
    Check if the combination of items in the backpack can save Amelia.

    Parameters:
    - backpack (list): The list representing the user's backpack.

    Returns:
    - bool: True if the combination is valid, False otherwise.
    """
    valid_combinations = [
        ["Matches", "Food"],
        ["Matches", "First Aid Kit", "Shelter Materials"],
        ["Water", "First Aid Kit", "Food"],
        ["Matches", "Knife", "Shelter Materials"],
        ["Water", "Shelter Materials"],
        ["Knife", "Compass", "Walkie Talkie"],
        ["Map", "Compass", "Water"]
    ]
    return backpack in valid_combinations



