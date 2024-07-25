# Welcome Stranger

# def greetings(name_list, job_dict):
#     part_1 = f"Hello, {' '.join(name_list)}! "

#     if job_dict['title'][0] in ['a', 'e', 'i', 'o', 'u']:
#         part_2 = "Nice to have an "
#     else:
#         part_2 = "Nice to have a "
    
#     part_3 = f"{job_dict['title']} {job_dict['occupation']} around."

#     return part_1 + part_2 + part_3

# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )
# print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

# Greeting a user

# user_name = input('What is your name? ')
# if user_name[-1] == '!': # could also use str.endswith("!")
#     print(f'HELLO {user_name.upper()} WHY ARE WE YELLING?')
# else:
#     print(f'Hello {user_name.capitalize()}.')

# Floating Point Arithmetic

# first_num = float(input("==> Enter the first number:\n"))
# second_num = float(input("==> Enter the second number: \n"))

# print(f"{first_num} + {second_num} = {first_num + second_num}")
# print(f"{first_num} - {second_num} = {first_num - second_num}")
# print(f"{first_num} * {second_num} = {first_num * second_num}")
# print(f"{first_num} / {second_num} = {first_num / second_num}")
# print(f"{first_num} // {second_num} = {first_num // second_num}")
# print(f"{first_num} % {second_num} = {first_num % second_num}")
# print(f"{first_num} ** {second_num} = {first_num ** second_num}")

# The End Is Near But Not Here

# def penultimate(string):
#     word_list = string.split(' ')  ## didn't need the ' ' bc default is to split on spaces
#     return word_list[-2]

# # These examples should pring True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# Exclusive Or

# def xor(arg1, arg2):
#     if (arg1 and not arg2) or (not arg1 and arg2):
#         return True
#     else:
#         return False

# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

# Odd Lists

# def oddities(my_list):
#     result = []

#     for index in range(len(my_list)):
#         if index % 2 == 0:
#             result.append(my_list[index])
    
#     return result

# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])
# print(oddities([1, 2, 3, 4]) == [1, 3])
# print(oddities(["abc", "def"]) == ['abc'])
# print(oddities([123]) == [123])
# print(oddities([]) == [])

# Odd Lists Bonus Question

# def oddities(my_list):
#     return my_list[::2]

# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])
# print(oddities([1, 2, 3, 4]) == [1, 3])
# print(oddities(["abc", "def"]) == ['abc'])
# print(oddities([123]) == [123])
# print(oddities([]) == [])

# How Old is Teddy?

# import random

# teds_age = random.randint(20, 100)

# print(f'Teddy is {teds_age} years old!')

# When Will I Retire?

# import datetime

# while True:
#     print()
#     current_age = input("What is your age? \n")

#     if current_age.isnumeric():
#         current_age = int(current_age)
#         break
#     else:
#         print()
#         print("**You must input an integer for your age.**")

# while True:
#     print()
#     retirement_age = input('At what age would you like to retire? \n')

#     if retirement_age.isnumeric():
#         retirement_age = int(retirement_age)
#         break

#     else:
#         print()
#         print("**You must input an integer for your retirement age.**")

# current_year = datetime.datetime.now().isocalendar().year
# years_left = retirement_age - current_age

# print()

# if years_left < 0:
#     print("Congratulations! You should have retired in "
#           f"{current_year + years_left}!")

# else:
#     print(f"It's {current_year}. " 
#           f"You will retire in {current_year + years_left}.")
#     print(f"You have only {years_left} years of work to go!\n")

# Get Middle Character

# def center_of(string):
#     string_len = len(string)
#     middle_index = string_len // 2

#     if string_len % 2 == 0:
#         return string[middle_index -1 : middle_index + 1]
#     else:
#         return string[middle_index]

# print(center_of('I Love Python!!!') == 'Py')
# print(center_of('Launch School') == ' ')
# print(center_of('Launchschool') == 'hs')
# print(center_of('Launch') == 'un')
# print(center_of('Launch School is #1') == 'h')
# print(center_of('x') == 'x')

# Always Return Negative

# def negative(num):
#     if num > 0:
#         return -1 * num
#     else:
#         return num
    
# print(negative(5) == -5)
# print(negative(-3) == -3)
# print(negative(0) == 0)