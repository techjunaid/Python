import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
rock'''

paper = ''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
paper'''

scissors = ''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
scissors'''

game_images = [rock, paper, scissors]

user_choice = int(input("what do you chose ? Type 0 for rock type 1 for paper type 2 for scissors \n"))
print("you chose ",game_images[user_choice])
computer_choice = random.randint(0,2)
print("computer chose :")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice <0:
    print(" You typed an invalid number ! You lose ")
elif user_choice == 0 and computer_choice==2 :
    print("You win")
elif computer_choice == 0 and user_choice == 2:
    print("You lose !")
elif computer_choice >user_choice :
    print("You losec !")
    
elif user_choice >computer_choice:
    print("You win !")
elif computer_choice == user_choice :
    print("it's a draw ")
