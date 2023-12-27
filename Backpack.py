'''
Date:03/08/23
Name: Shravan Agnihotri
Description: This program will setup a story, where the user is responsible for saving someone stuck at seas.
The user will have a choice from 10 items to bring. Choosing the correct combination of items will ensure their safety. 
Extra Features: Taking Out and Editing Items, still being worked on.
'''

# Import Time Module 
import time 

#Initialize Variables
Continue = False
delay = 0.00001

# Initialize Lists
validItems = ["Water","Knife","Matches","Shelter Materials","First Aid Kit","Food","Compass","Walkie Talkie","Map", "Money",]
backpack = []

# Initialize Strings That Must Be Delayed Using Time Module
validItems2 = """
Water, 
Knife, 
Matches, 
Shelter Materials, 
First Aid Kit, 
Food, 
Compass, 
Walkie Talkie, 
Map, 
Money
"""

backstory = """
In the middle of a huge ocean, there was a mysterious island hidden in mist and filled with secrets. 
One day, a curious traveler named Amelia decided to explore it. Her ship got caught in a storm, 
and she ended up on the island's shore. But the island's secrets were hard to grasp, 
and Amelia's destiny got lost with its mysteries. 
You must help Amelia by bringing her 3 items from your backpack, which could or could not save her. 
"""

Travels ="""
Gathering resources for your journey...
Loading your character's equipment...
"""

congrats = """
Amelia Used Your Resources
Lucky for her, you chose the right items and...
SHE SURVIVED! Congratulations, you saved Amelia!
"""

death = """
Amelia Used Your Resources.
Unfortunatley for her, you chose the wrong items and...
SHE DIED! You could not save her from the mysterious Island.
"""

# Function makes the text print out on screen over time. Takes in 2 arguments (Speed, Words)
def intro(delay, text):
     for char in text:
          print(char, end = '', flush=True)
          time.sleep(delay)
          
# Function makes takes user to Island stage of the game.    
def Island():
     delay = 0.2
     print("Time To Save Amelia...Lets Head To The Island")
     intro(delay, Travels)
     print("You Have Arrived At The Island!")
     checker()

# Function Checks to see if items are good enough to save Amelia
def checker():
        delay = 0.1
        if ("Matches" in backpack and "Food" in backpack):
            intro(delay, congrats)
        elif("Matches" in backpack and "First Aid Kit" in backpack and "Shelter Materials" in backpack):
            intro(delay, congrats)
        elif("Water" in backpack and "Fist Aid Kit" in backpack and "Food" in backpack):
            intro(delay, congrats)
        elif("Matches" in backpack and "Knife" in backpack and "Shelter Materials" in backpack):
            intro(delay, congrats)
        elif("Water" in backpack and "Shelter Materials" in backpack):
            intro(delay, congrats)
        elif("Knife" in backpack and "Compass" in backpack and "Walkie Talkie" in backpack):
            intro(delay, congrats)
        elif("Map" in backpack and "Compass" in backpack and "Water" in backpack):
            intro(delay, congrats)
        else:
            intro(delay, death)

# Function Allows User to edit their backpack (still working on) 
def remove():
    remove = int(input("What Item Would You Like to Remove From Your Backpack?\nEnter 0 for Item 1\nEnter 1 for Item 2\nEnter 2 for Item 3\n"))
    if (remove==0 or remove==1 or remove ==2):
        removeItem = backpack.pop(remove)
        print("You are removing", removeItem)
        print("Your updated backpack is", backpack)
    else:
        print("Invalid Input, Please Enter Either 0,1,2\n")
        remove = int(input("What Item Would You Like to Remove From Your Backpack?\nEnter 0 for Item 1\nEnter 1 for Item 2\nEnter 2 for Item 3\n"))
        if (remove==0 or remove==1 or remove ==2):
            removeItem = backpack.pop(remove)
            print("You are removing", removeItem)
            print("Your updated backpack is", backpack)
            
            
# Calls an introduction function to present backstory and items
intro(delay, backstory)
print("------------------------------------------------------------------------------------------------------")
print("These are the items you can choose from:")
intro(delay, validItems2)
         
     

# Ask them to add their first item.
item1 = input(str("\nWhat is the first item that you would like to add to your backpack? "))


if item1 in validItems:
        backpack.append(item1)
        print("Your Item Has Been Succesfully Added.")
        print("Your updated backpack looks like this", backpack)
else: 
    while(item1 not in validItems):
        print("Invalid Item, Please Try Again.")
        item1 = input(str("What item that you would like to add to your backpack? "))

        if item1 in validItems:
            backpack.append(item1)
            print("Your Item Has Been Succesfully Added.")
            print("Your updated backpack looks like this", backpack)

# Asks them second item
item2 = input(str("\nWhat is the second item that you would like to add to your backpack? "))

if item2 in validItems:
        backpack.append(item2)
        print("Your Item Has Been Succesfully Added.")
        print("Your updated backpack looks like this", backpack)
else: 
    while(item2 not in validItems):
        print("Invalid Item, Please Try Again.")
        item2 = input(str("What item that you would like to add to your backpack? "))

        if item2 in validItems:
            backpack.append(item2)
            print("Your Item Has Been Succesfully Added.")
            print("Your updated backpack looks like this", backpack)

# Asks them for 3rd Item
item3 = input(str("\nWhat is the third item that you would like to add to your backpack? "))

if item3 in validItems:
        backpack.append(item3)
        print("Your Item Has Been Succesfully Added.")
        print("Your updated backpack looks like this", backpack)
else: 
    while(item3 not in validItems):
        print("Invalid Item, Please Try Again.")
        item3 = input(str("What item that you would like to add to your backpack? "))

        if item3 in validItems:
            backpack.append(item3)
            print("Your Item Has Been Succesfully Added.")
            print("Your updated backpack looks like this", backpack)

# Gives User a Choice To Edit Their Backpack or Continue in the story.
print("------------------------------------------------------------------------------------------------------\n")
Choice = (input("Would You Like To Continue Your Journey and Bring Amelia Your Backpack?\nType Yes to Continue and Type No to edit your backpack\n"))
if (Choice == "Yes"):
    print("Your Final Backpack looks like this", backpack)
    Island()
elif(Choice == "No"):
    remove()

