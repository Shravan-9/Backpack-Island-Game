import time

def setup_story():
    """
    Return the setup for the story.

    Returns:
    - str: The backstory setup for the game.
    """
    return """
In the middle of a huge ocean, there was a mysterious island hidden in mist and filled with secrets. 
One day, a curious traveler named Amelia decided to explore it. Her ship got caught in a storm, 
and she ended up on the island's shore. But the island's secrets were hard to grasp, 
and Amelia's destiny got lost with its mysteries. 
You must help Amelia by bringing her 3 items from your backpack, which could or could not save her.
"""

def valid_items():
    """
    Print the list of valid items to choose from.

    Returns:
    - str: The formatted string containing the valid items.
    """
    valid_items = ["Water", 
                   "Knife", 
                   "Matches", 
                   "Shelter Materials", 
                   "First Aid Kit", 
                   "Food", 
                   "Compass", 
                   "Walkie Talkie", 
                   "Map", 
                   "Money"]
    
    formatted_items = "\n".join(valid_items)
    return f"These are the items you can choose from:\n{formatted_items}\n"


def setup_journey():
    """
    Return additional setup for the journey.

    Returns:
    - str: The setup for the character's journey.
    """
    return """
Gathering resources for your journey...
Loading your character's equipment...
"""

def congratulatory_message():
    """
    Return the congratulatory message.

    Returns:
    - str: The message for a successful outcome.
    """
    return """
Amelia Used Your Resources
Lucky for her, you chose the right items and...
SHE SURVIVED! Congratulations, you saved Amelia!
"""

def death_message():
    """
    Return the death message.

    Returns:
    - str: The message for an unsuccessful outcome.
    """
    return """
Amelia Used Your Resources.
Unfortunately for her, you chose the wrong items and...
SHE DIED! You could not save her from the mysterious Island.
"""


def print_with_delay(delay, text):
    """
    Print each character in 'text' with a delay.

    Parameters:
    - delay (float): The delay between each character.
    - text (str): The text to be printed with a delay.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def intro(delay, text):
    """
    Display an introduction with a delayed print.

    Parameters:
    - delay (float): The delay between each character.
    - text (str): The introduction text to be displayed.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def get_user_input(prompt):
    """
    Get user input with a specified prompt.

    Parameters:
    - prompt (str): The prompt to be displayed to the user.

    Returns:
    - str: The user's input.
    """
    return input(f"{prompt} ").strip()  # Add .strip() to remove leading/trailing whitespaces

def get_user_input_no_prompt():
    """
    Get user input without a prompt.

    Returns:
    - str: The user's input.
    """
    return input().strip()


def display_backpack(backpack):
    """
    Display the current contents of the user's backpack.

    Parameters:
    - backpack (list): The list representing the user's backpack.
    """
    print("Your current backpack is", backpack)

def ask_for_item(index):
    """
    Ask the user for an item to add to the backpack.

    Parameters:
    - index (int): The index of the item being asked for.

    Returns:
    - str: The user's input for the item.
    """
    return input(f"What is the item {index + 1} that you would like to add to your backpack? ")

def ask_continue_journey():
    """
    Ask the user if they want to continue the journey.

    Returns:
    - str: The user's input indicating whether they want to continue or not.
    """
    return input("Would you like to continue your journey and bring Amelia your backpack?\nType 'Yes' to continue and 'No' to edit your backpack\n")
