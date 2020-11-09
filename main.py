import sys
import random
Intro = "Welcome to the Decision Maker"
desc = "This program will help you make a decision"
notDone  = True
newlist = []
print(Intro)
print(desc)

while notDone:
    
    print("Please enter your choices.\nEnter done when complete.")
    user_input = input()
    if user_input == 'done':
        notDone = False
    else:
        newlist.append(user_input)

else:
    print("Thank you for letting us decide")
    print("Here is our choice: "+newlist[random.randint(0,len(newlist)-1)])