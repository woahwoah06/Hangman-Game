import time
import random


# Initializing variables/lists

with open("words.txt", "r") as file:
    word_list = file.read().splitlines()   # imports list of words

remain = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']   # remaining letters
used = []   # used letters
temp = []

char = None
word = None
victory = None
player_guess = None
repeat = 'Y'
lives = 10
turns = 1


# Defining functions

def intro():
    
    print('Greetings! Welcome to the Hangman Game!')
    print('\nYou will have to try to guess a random word by selecting a letter.')
    print('If the letter you have chosen appears in the word, it will be revealed.')
    print('\nYou only get 10 incorrect guesses before you lose, good luck!')

    time.sleep(1)


def game():

    global word, lives, victory, repeat, turns

    print('\n--------------------------------------------------------')
    print('(Start)') 
    print('I am thinking of a word...')

    word = random.choice(word_list)

    while len(word) not in range(5, 16):   # only selects a word between 5 - 15 characters
        word = random.choice(word_list)
        
    time.sleep(1)

 
    while victory == None:   # runs until player wins/loses

        make_guess()

        
    print('\n--------------------------------------------------------')
    print('(End Result)\n')
    time.sleep(1)
    
    if victory == 'Y':   # if player wins
        
        if lives == 10:
            print('Congratulations for guessing the word without losing any lives! Crazy luck!')

        elif lives in range(2,10):
            print(f'Well done! You guessed the word with {lives} lives left.')

        elif lives == 1:
            print('Close call! You guessed the word with 1 life left.')

    else:   # if player loses

        print('Game over! You lost all your lives.')
        print('\nThe word was:', word)
        

    print('\n--------------------------------------------------------')
    repeat = input('Would you like to play again? (Y/N): ').upper().strip()    # asks user if repeat

    while repeat not in ('Y','N'):
        repeat = input('INVALID! Would you like to play again? (Y/N): ').upper().strip()

    if repeat == 'N':    # exits game()
        return

    # resets variables before repeat
    lives = 10
    turns = 1
    victory = None

    remain = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    used = []


def make_guess():

    global lives, victory, turns

    remain_out = str(remain).replace("'","")   # makes remain suitable as output
    temp = []   # resets temp


    print('\n--------------------------------------------------------')
    print(f'(Turn #{turns})')
    print(f'Here are your remaining letters:\n{remain_out}\n')

    for i in range(len(word)):   # hides/reveals letters in the word

        char = word[i]

        if char in remain:
            temp.append('_')

        else:
            temp.append(char)

    print('Word:', ''.join(temp))   # prints the shown word


    if '_' not in temp:   # checks if player has fully guessed word
        
        victory = 'Y'
        return   # exits make_guess()

    
    player_guess = str(input('\nEnter your guess: ')).lower().strip()

    return player_guess
  
    while player_guess not in remain:                                              # checks if letter has been used
        player_guess = str(input('INVALID! Enter your guess: ')).lower().strip()

    if player_guess in word:
        print(f'\n{player_guess} is in the word!')

    elif player_guess not in word:
        print(f'\n{player_guess} is not in the word!')
        lives -= 1


    remain.remove(player_guess)   # updates lists
    used.append(player_guess)

    used_out = str(used).replace("'","")   # makes used suitable as output

    print('\nUsed letters:', used_out)
    print('Lives left:', lives)

    if lives == 0:   # if player loses all lives

        victory = 'N'

    turns += 1


# Running game

intro()

while repeat == 'Y':
    
    game()


print('\nThanks for playing.')   # if player doesnt want to repeat
time.sleep(1.5)

exit()
