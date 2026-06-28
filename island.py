print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('Choose "left" or "right": ')

if choice1 == "left":
    choice2 = input('Choose "swim" or "wait": ')

    if choice2 == "wait":
        choice3 = input('Choose a door: "red", "blue", or "yellow": ')

        if choice3 == "red":
            print("Game Over")
        elif choice3 == "yellow":
            print("You Win!")
        else:
            print("Game Over")

    else:
        print("Game Over")

else:
    print("Game Over")

