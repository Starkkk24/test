r=("""chose Rock.
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

p=("""chose Paper.
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

s=("""chose Scissor.
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
lst=[r,p,s]
user=int(input("Choose:\n0 for Rock\n1 for Paper\n2 for Scissor\n: "))
print(f"You {lst[user]} ")

import random
comp = random.randint(0,2)
print(f"Computer {lst[comp]}")

if user==0 and comp==2:
    print("Yeheeh!!\nYou Won!")
elif user==1 and comp==0:
    print("Yeheeh!!\nYou Won!")
elif user==2 and comp==1:
    print("Yeheeh!!\nYou Won!")
elif user==comp:
    print("== Draw ==")
else:
    print("Better luck next time! :x")