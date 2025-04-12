#********** TREASURE ISLAND GAME **********/
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Choose direction
direction = input("Do you want to go left or right?\n").lower() #Convert all user input to lower case

# if direction == "left" or direction == "Left" or direction == "LEFT"
if direction == "left":
    #continue in  game
    #Prompt the user if they chose to swim or wait
    decision = input("Would you like to swim or wait?\n").lower()
    if decision == "wait":
        door = input("Which door would you like to go through: "
                     "'Red', 'Yellow' or 'Blue'\n").lower()
        if door == "red":
            print("Burned by fire. \n GAME OVER!")
        elif door == "blue":
            print("Eaten by beasts. \n GAME OVER!")
        elif door == "yellow":
            print("YOU WIN!")
        else:
            print("GAME OVER!")
    elif decision == "swim":
        print("Attacked by trout. \nGAME OVER!")
    else:
        print("GAME OVER!")
elif direction == "right":
    print("Fall into a hole. \nGAME OVER!")
else:
    print("Please input 'left' or 'right'")
