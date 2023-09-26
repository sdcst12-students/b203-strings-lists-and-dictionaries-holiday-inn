#!python3
"""
##### Task 5
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

possible items:
food  fud
water -> wtr
rope -> rop
torch ->tch
sack -> sak
wood -> wud
iron -> irn
steel -> stl
ginger -> gng
garlic -> gar 
fish -> fsh
stone -> stn
wool ->wul

example:
>get food
>get water
>get water
>get iron
>get 3 wood
>inventory
You have:
 1 food
 2 water
 1 iron
 3 wood
 >
"""
f = True
subnames = {
    "food" : "fud",
"water" : "wtr",
"rope" : "rop",
"torch" :"tch",
"sack" : "sak",
"wood" : "wud",
"iron" : "irn",
"steel" : "stl",
"ginger" : "gng",
"garlic" : "gar",
"fish" : "fsh",
"stone" : "stn",
"wool" : "wul",
}
dict = {
    "food" : 0,
    "water":0,
"rope":0,
"torch":0,
"sack":0,
"wood":0,
"iron":0,
"steel":0,
"ginger":0,
"garlic":0,
"fish":0,
"stone":0,
"wool" : 0

}

while f == True:
    action = input(">")
    action = action.split(" ")
    if action[0] == "get":
        if action[1] in dict:
            dict[action[1]]+=1
        else: print("enter something real")
        print(f"you now have {dict[action[1]]}")
    elif action[0] == "drop":
        if dict[action[1]] == 0:
            print("you cant do that")
        else:
            if action[1] in dict:
                dict[action[1]]-=1
            else: print("enter something real")
            print(dict[action[1]])
    elif action[0] == "inv" or action[0] == "inventory":
        for i in dict:
            if dict[i] >0:
                print("you have: ")
                print(f" {dict[i]} {i}")
    elif action[0] == "exit":
        break
    else:
        print("not a valid action")

