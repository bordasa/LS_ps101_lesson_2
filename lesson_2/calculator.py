import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Set the language
lang = 'ENG'

# Get the message from the JSOON file
def messages(message):
    return MESSAGES[lang][message]

# Convert message into the prompt
def prompt(message):
    print(f"==> {message}")

# To validate the input
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

# Quick function for improving readability
def draw_line():
    print('------------------------------')

# Main program
calculating = True

while calculating == True:
    draw_line()
    prompt(messages('welcome'))
    draw_line()
    print()

    # Ask the user for the first number.
    prompt(messages('question_1'))
    number1 = input()

    while invalid_number(number1):
        prompt(messages('sorry'))
        number1 = input()

    # Ask the user for the second number.
    prompt(messages('question_2'))
    number2 = input()

    while invalid_number(number2):
        prompt(messages('sorry'))
        number2= input()

    # Ask the user for an operation too perform.
    while True:

        prompt(messages('question_3'))
        operation = input()

        if operation not in ['1', '2', '3', '4']:
            draw_line()
            prompt(messages('correct_choices_1'))
            draw_line()
            print()
        else:
            break

    # Perform the operation on the two numbers.
    match operation:
        case '1':
            result = float(number1) + float(number2)
        case '2':
            result = float(number1) - float(number2)
        case '3':
            result = float(number1) * float(number2)
        case '4':
            result = float(number1) / float(number2)

    # Print the result to the terminal.
    draw_line()
    prompt(messages('result').format(result))
    draw_line()
    print()

    while True:
        draw_line()
        prompt(messages('restart'))
        print()
        does_user_continue = input()

        if does_user_continue == '1':
            break
        if does_user_continue == '2':
            calculating = False
            print()
            draw_line()
            prompt(messages('thank_you'))
            draw_line()
            print()
            break
        else:
            draw_line()
            prompt(messages('correct_choices_2'))
            draw_line()
            print()
            prompt(messages('press_any_key'))
            input()