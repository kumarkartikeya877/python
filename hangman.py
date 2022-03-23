from hangman_word import word_list
from hangman_ui import stages
from hangman_ui import logo
import random
print(logo)
choosed_word = random.choice(word_list)


display = []
for i in range(0,len(choosed_word)):
    display += "_"
print(display)

game_end = False
life = 6

while game_end == False:
    guess = input("enter guess : ").lower()
    if guess in display:
        print(f"you already guessed {guess}")
    for i in range (len(choosed_word)):
        if guess == choosed_word[i]:
            display[i]= guess
    if guess not in choosed_word:
        life -= 1
        print("wrong guess.You lose a life.")
        
    print(display)
    print(stages[life])
    if "_" not in display:
        game_end = True
        print("___YOU WIN___")
    elif life==0:
        game_end = True
        print("___YOU LOSE___")

    
    
