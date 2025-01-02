# requisites
lst=["hammer","elephant","pepper"]
Stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random
chosen_wrd=random.choice(lst)
print(chosen_wrd)

# initializing the "_"s, to know the no. of letters in the word
under=""
for i in range(len(chosen_wrd)):
    under += "_ "
print(under)

# defining needs/constraints
crrct_wrd=[]
lives=6  
game_over = False

# main funciton
while not game_over:
    # to initiate display word and let the matching letters get placed
    display_wrd=""
    guess=input("Guess a letter: ")
    for x in chosen_wrd:
        if guess == x:
            display_wrd += x+" "
            crrct_wrd.append(guess)
        elif x in crrct_wrd:
            display_wrd += x+" "
        else:
            display_wrd += "_ "
    print(display_wrd)

    # to subtract the life if the letter doesn't match, n decide if lives==0 => Game over => LOOSE!
    if guess not in chosen_wrd:
        lives -= 1
        if lives == 0:
            game_over=True
            print("You Loose")
    
    # if all the correct letters are placed => there is no "_ " => Game over => WON!
    if "_ " not in display_wrd:
        game_over = True
        print("You Won")
    
    # to pirnt the graphic symbol (for remaining lives)
    print(Stages[-lives])