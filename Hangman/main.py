"""
Game hangman 1.0
1) chose a word from list
2) display the letters of the chosen word as ----
3) input a letter from user and check the positions if any
    a) if not => 1 life lost and check if any life left
    b) if yes => change the positions from "-" to "the letter" and check if any "-" left
4) step 3) again until no life or no "-" left
5) gameover => win / loss
"""

import random
import os
from hangman_art import life, logo


with open("hangman_words.txt") as f:
    word_list = f.read().splitlines()


def main():
    play = 1

    while play == 1:
        word_chosen = random.choice(word_list)
        word_displayed = len(word_chosen) * ["-"]
        lives = 6

        while "-" in word_displayed:
            print(logo[0])
            print(life[lives])
            print(word_displayed)
            chosen_letter = input("Choose a letter: ").lower()
            os.system('cls' if os.name == 'nt' else 'clear')

            for position in range(len(word_chosen)):
                if word_chosen[position] == chosen_letter:
                    word_displayed[position] = word_chosen[position]
            if chosen_letter not in word_chosen:
                lives -= 1
            if lives == 0:
                break

        print(logo[0])
        if word_chosen == "".join(word_displayed):
            print("You have won!")
        else:
            print("You have lost")
            print(f"The word was: {word_chosen}")
        play = int(input("Play again? (1=Yes, 0=No): "))
        os.system('cls' if os.name == 'nt' else 'clear')


main()
