import random
user_choice = int(input("enter ur choice \n 0 = Rock \n 1 = Paper\n 2= Scissors:"))
if(user_choice>=3 or user_choice <0):
    print("invalid number, enter again...!")
else:
    computer_choice = random.randint(0,2)
    print(f"the user chose:{user_choice}")
    print(f"the computer chose:{computer_choice}")
    if(user_choice == computer_choice):
        print("It is draw.........😊😇")
    elif (computer_choice == 2 and user_choice == 0):
        print("You Win....🥳")
    elif (user_choice == 2 and computer_choice == 0):
        print("You Lose....😔")
    elif(computer_choice>user_choice):
        print("You Lose....😔")
    elif(user_choice>computer_choice):
        print("You Win....🥳")
