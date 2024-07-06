import random

VALID_CHOICES = ['rock', 'paper', 'scissors']
PLAY = True
ROUND_COUNTER = 1
COMPUTER_SCORE = 0
PLAYER_SCORE = 0
TIE_SCORE = 0

def draw_line():
    print("=====================================================")

def prompt(message):
    print(f"==> {message}")

def welcome_message():
    print()
    draw_line()
    print("         Welcome to Rock, Paper, Scissors           ")
    draw_line()
    print()

def update_score():
    global ROUND_COUNTER
    prompt(f'Rounds: {ROUND_COUNTER}')
    prompt(f'Your Score: {PLAYER_SCORE}')
    prompt(f"Computer's Score: {COMPUTER_SCORE}")
    prompt(f'Ties: {TIE_SCORE}')
    draw_line()

def display_winner(answer, computer_answer):
    global PLAYER_SCORE, COMPUTER_SCORE, TIE_SCORE

    prompt(f'You selected {answer}. Computer selected {computer_answer}.')
    print()
    
    if answer == computer_answer:
        prompt('The game is a tie!\n')
        TIE_SCORE += 1
    elif ((answer == 'rock' and computer_answer == 'scissors')
          or (answer == 'paper' and computer_answer == 'rock')
          or (answer == 'scissors' and computer_answer == 'paper')):
        prompt(f'You win!\n')
        PLAYER_SCORE += 1
    else:
        prompt(f'The computer wins!\n')
        COMPUTER_SCORE += 1
    
    update_score()

while PLAY == True:

    welcome_message()

    prompt(f'Please make a choice: {", ".join(VALID_CHOICES)}')
    answer = input('    ').lower()

    while answer not in VALID_CHOICES:
        prompt('==>Please type a valid response.')
        answer = input('    ').lower()

    computer_answer = random.choice(VALID_CHOICES)

    display_winner(answer, computer_answer)

    while True:
        prompt('Would you like to play again? (y/n)')
        play_again = input('    ')

        if play_again[0] == 'n':
            prompt('Thank you for playing.')
            draw_line()
            PLAY = False
            break
        elif play_again[0] == 'y':
            draw_line()
            ROUND_COUNTER += 1
            break
        else:
            prompt('==>Please input "y" (yes) or "n" (no).')
        
        draw_line()