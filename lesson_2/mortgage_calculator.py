def prompt(message):
    print(f'==> {message}')

def draw_line():
    print('===================================================')

# Used to validate input
def invalid_number(number_str):
    try:
        number = float(number_str)
        if number < 0:
            draw_line()
            prompt('Error: value must be greater than 0.')
            draw_line()
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True

    return False

# Welcome to the app
draw_line()
prompt('Welcome to the Mortgage Calculator')

# Ask for the load amount
draw_line()
prompt('Please input the loan amount (do not use commas):')
prompt('    Example: 500000 or 500_000\n')
loan_amount = input('        $')

while invalid_number(loan_amount):
    prompt('Please input a valid loan amount.')
    loan_amount = input('        $')

# Ask for the APR
draw_line()
prompt('Please input the Annual Percentage Rate (APR).')
prompt('    Example: input 5 for 5%\n')
apr = input('        ')

while invalid_number(apr):
    prompt('Please input a valid APR.')
    apr = input('        ')

# Convert APR to decimal
apr = float(apr) / 100

# Ask for the loan duration
draw_line()
prompt('Please input the loan duration (in years).\n')
duration_years = input('        ')

while invalid_number(duration_years):
    prompt('Please input a valid number of years.')
    duration_years = input('        ')


# Calculate monthly interest rate
interest_monthly = apr / 12
# Calculate loan duration in months
duration_months = float(duration_years) * 12

# Calculate the monthly payment
if apr == 0:
    payment_monthly = float(loan_amount) / duration_months
else:
    payment_monthly = float(loan_amount) * (interest_monthly /
                    (1 - (1 + interest_monthly) ** (-duration_months)))


payment_monthly = round(payment_monthly, 2)

draw_line()
prompt(f'Your monthly payment is ${payment_monthly}')
draw_line()