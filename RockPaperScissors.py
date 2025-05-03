import random
print("Mohd Jawwad Ali Farooqui,USN:1AY24AI070,SEC:O")
name=input("Enter the name of the player:")
choice=int(input("Enter any one of the below(1-ROCK,2-PAPER,3-SCISSORS):"))
while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice please"))
if choice == 1:
        choice_n = 'Rock'
elif choice == 2:
        choice_n = 'Paper'
else:
     choice_n = 'Scissors'
print(name,"choice is:", choice_n)
print("Now its computer turn")
comp_choice= random.randint(1, 3)
if comp_choice == 1:
        comp_choice_name = 'Rock'
elif comp_choice == 2:
        comp_choice_name = 'Paper'
else:
    comp_choice_name = 'Scissors'
print("Computer choice is:", comp_choice_name)
if choice == comp_choice:
        result = "Draw"
elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = 'Paper'
elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = 'Rock'
elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = 'Scissors'
if result=="Draw":
    print("It's a tie!")
elif result == choice_n:
    print(name,"is the Winner")     
else:
    print("Computer wins!")
