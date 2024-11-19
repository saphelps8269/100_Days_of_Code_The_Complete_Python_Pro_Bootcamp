print("Welcome to Booby Trap Island.")
print("Your mission is to find the treasure.")

# choice1
choice1 = input("You are at a cross roads. Do you want to go left or right? Type left or right: ").lower()

if choice1 == "left":
    print("You walked left.")

    # choice2
    choice2 = input("You come to a river. Do you swim or wait? Type swim or wait: ").lower()
    if choice2 == "wait":
        print("You waited for a boat.")

        # choice3
        choice3 = input("You come to 3 doors: red, blue, and yellow. Which color do you choose? ").lower()
        if choice3 == "yellow":
            print("You win!")
        elif choice3 == "blue":
            print("There was a werewolf. You were eaten. Game over.")
        elif choice3 == "red":
            print("There was a fire behind the door. You burned up. Game over.")
        else:
            print("You died of starvation. Game over.")
    elif choice2 == "swim":
        print("Overrun by trout. Game over.")
else:
    print("You fell in a hole. Game over.")