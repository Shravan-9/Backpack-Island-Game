'''
Name: Shravan Agnihotri
Description: This program will setup a story, where the user is responsible for saving someone stuck at seas.
The user will have a choice from 10 items to bring. Choosing the correct combination of items will ensure their safety. 
Extra Features: Taking Out and Editing Items, still being worked on.
'''
# Import Modules and Libaries
import time
import prompts
import backpack_functions

# Introduction
prompts.intro(0.01, prompts.setup_story())
print("------------------------------------------------------------------------------------------------------")
prompts.intro(0.01, prompts.valid_items() )

backpack = []

# Ask the user to add 3 items to the backpack
for i in range(3):
    item = prompts.get_user_input_no_prompt(prompts.ask_for_item(i))

    while item not in backpack_functions.validItems:
        print("Invalid Item, Please Try Again.")
        item = prompts.get_user_input_no_prompt(prompts.ask_for_item(i))

    backpack = backpack_functions.add_item(backpack, item)
    print("Your Item Has Been Successfully Added.")
    prompts.display_backpack(backpack)

# Ask the user to continue the journey or edit the backpack
print("------------------------------------------------------------------------------------------------------\n")
Choice = prompts.ask_continue_journey()

if Choice.lower() == "yes":
    print("Your Final Backpack looks like this", backpack)
    if backpack_functions.check_combinations(backpack):
        prompts.print_with_delay(0.1, prompts.congratulatory_message())
    else:
        prompts.print_with_delay(0.1, prompts.death_message())
else:
    index = int(prompts.get_user_input("Enter the index of the item you want to remove: "))
    removed_item, backpack = backpack_functions.remove_item(backpack, index)

    if removed_item is not None:
        print(f"You have removed {removed_item}. Your updated backpack is {backpack}")
    else:
        print("Invalid index. Please try again.")
