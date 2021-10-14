print("Welcome to Treasure Island\nYour Mission is to Find the treasure")
road = input("You are at a cross road. Where do you want to go ? Type Left or Right ? :: ").lower()

if road == "left":
    choice2 = input('''you want "wait" or "swim" ? :: ''').lower()
    if choice2 == "wait":
        choice3 = input("which door you want open, Red , Blue , Yellow ? :: ").lower()
        if choice3 == "yellow":
            print("you find the treasure and you won ")
        else:
            print("you caught by ghost, Game Over")
    else:
        print("You are struct Game Over !") 
        
    
else:
    print("Game over !!")
    
    
