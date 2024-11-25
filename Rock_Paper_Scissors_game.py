print(" The Rock,Paper,Scissors Game")
import random
weapons=["Rock","Paper","Scissors"]
print(weapons)
a=input("enter your weapon: ")
x=random.choice(weapons)
print(f"user chose{a}, bot chose{x}")
if (a==x):
    print("same weapons collapsed! It's a Draw")
elif (a=="Rock" and x=="Paper"):
    print("Bot Wins....")
elif (a=="Rock" and x=="Scissors"):
    print("You Win!!")
elif (a=="Paper" and x=="Rock"):
    print("You Win!!")
elif (a=="Paper" and x=="Scissors"):
    print("Bot Wins....")
elif (a=="Scissors" and x=="Rock"):
    print("Bot Wins....")
elif (a=="Scissors" and x=="Paper"):
    print("You Win!!")
    