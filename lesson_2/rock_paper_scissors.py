import random

WINNING_COMBOS = {
    'rock':     ['lizard',   'scissors'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['spock',    'paper'],
    'spock':    ['scissors', 'rock']
}

SHORT_VALID_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
    'l': 'lizard',
    'k': 'spock'
    }

PLAY = True
ROUND_COUNTER = 1
COMPUTER_SCORE = 0
PLAYER_SCORE = 0
TIE_SCORE = 0

def draw_line():
    print("=============================================================")

def prompt(message):
    print(f"==> {message}")

def display_welcome_message():
    print()
    draw_line()
    print("             Welcome to Rock, Paper, Scissors           ")
    draw_line()
    print()

def determine_winner(answer, computer_answer):
    global PLAYER_SCORE, COMPUTER_SCORE, TIE_SCORE

    if computer_answer in WINNING_COMBOS[answer]:
        COMPUTER_SCORE += 1
        return 'computer'
    elif answer in WINNING_COMBOS[computer_answer]:
        PLAYER_SCORE += 1
        return 'player'
    else:
        TIE_SCORE += 1
        return 'tie'

def display_score():
    global ROUND_COUNTER
    prompt(f'Rounds: {ROUND_COUNTER}')
    prompt(f'Your Score: {PLAYER_SCORE}')
    prompt(f"Computer's Score: {COMPUTER_SCORE}")
    prompt(f'Ties: {TIE_SCORE}')
    draw_line()

def display_winner(answer, computer_answer):

    prompt(f'You selected {answer}. Computer selected {computer_answer}.')
    print()

    winner = determine_winner(answer, computer_answer)

    if winner == 'tie':
        prompt('The game is a tie!\n')
    elif winner == 'player':
        prompt('You win!\n')
    else:
        prompt('The computer wins!\n')

def play_again():
    global ROUND_COUNTER, PLAY
    
    while True:
        prompt('Would you like to play again? (y/n)')
        play_again = input('    ')

        if play_again != '' and play_again[0] == 'n':
            prompt('Thank you for playing.')
            draw_line()
            PLAY = False
            break
        elif play_again != '' and play_again[0] == 'y':
            draw_line()
            ROUND_COUNTER += 1
            break
        else:
            prompt('** Please input "y" (yes) or "n" (no). **')

# Game Play Loop
while PLAY is True:

    display_welcome_message()

    while True:
        prompt(f'Please make a choice: {", ".join(WINNING_COMBOS)}')
        player_choice = input('    ').lower()

        if player_choice in WINNING_COMBOS:
            break
        elif player_choice in SHORT_VALID_CHOICES:
            player_choice = SHORT_VALID_CHOICES[player_choice]
            break
        else:
            prompt('** Please type a valid response. **')

    computer_choice = random.choice(list(WINNING_COMBOS.keys()))

    display_winner(player_choice, computer_choice)

    display_score()

    play_again()

    draw_line()