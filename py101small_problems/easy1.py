# isn't it odd

# def isnt_it_odd(int):
#     if abs(int) % 2 != 0:
#         return True
#     else:
#         return False

# print(isnt_it_odd(3))
# print(isnt_it_odd(4))
# print(isnt_it_odd(5))

# Odd Numbers

# for num in range(1, 100):
#     if num % 2 != 0:
#         print(num)

# for num in range(1, 100, 2):
#     print(num)

# How big is the room?
# while True:
#     print("Please enter the length of the room (in meters):")
#     length = input()
    
#     if length.isnumeric() and float(length) > 0:
#         break
#     else:
#         print("Invalid length.")

# while True:
#     print("Please enter the width of the room (in meters):")
#     width = input()

#     if width.isnumeric() and float(width) > 0:
#         break
#     else:
#         print("Invalid width.")

# area_m2 = float(length) * float(width)
# area_ft2 = area_m2 * 10.7639

# area_m2 = round(area_m2, 2)
# area_ft2 = round(area_ft2, 2)

# print(f"The area of the room is {area_m2} sq meters ({area_ft2} sq ft).")

# LS solution specifies the formatting of the decimals in the output string
# print(f'The area of the room is {area_m2 :.2f} sq meters or'
#        f' {area_ft2 :.2f} sq feet.')

# Tip Calculator

# bill = input('What is the bill? ')
# tip_percent = input('What is the tip percentage? ')

# tip = float(bill) * float(tip_percent) / 100
# total = float(bill) + tip

# print()
# print(f'The tip is ${tip :.2f}')
# print(f'The total is ${total :.2f}')

# Sum or Product of Consecutive Integers
# top_num = int(input('Please enter an integer greater than 0:\n'))
# sum_or_prod = input('Enter "s" to compute the sum, or "p" to compute the product.\n')
# result = top_num

# if sum_or_prod == 's':
#     for num in range(1, top_num):
#         result += num

#     print(f'The sum of the integers between 1 and {top_num} is {result}.')

# if sum_or_prod == 'p':
#     for num in range(1, top_num):
#         result *= num
        
#     print(f'The product of the integers between 1 and {top_num} is {result}.')

# def short_long_short(string1, string2):
#     if len(string1) < len(string2):
#         return string1 + string2 + string1
#     if len(string2) < len(string1):
#         return string2 + string1 + string2

# # These examples should all print True
# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

# Leap Years (Part 1)

# def is_leap_year(year):
#     if year < 0:
#         print('Invalid year -- choose a year greater than 0')
#     else:
#         if year % 400 == 0:
#             return True
#         elif year % 100 == 0:
#             return False
#         elif year % 4 == 0:
#             return True
#         else:
#             return False
        
# # These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == False)
# print(is_leap_year(1100) == False)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == False)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# Leap Years (Part 2)

# def is_leap_year(year):
#     if year < 0:
#         print('Invalid year -- choose a year greater than 0')
#     elif year < 1752:
#         return year % 4 == 0
#     else:
#         if year % 400 == 0:
#             return True
#         elif year % 100 == 0:
#             return False
#         elif year % 4 == 0:
#             return True
#         else:
#             return False

# # These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == True)
# print(is_leap_year(1100) == True)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == True)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# Multiples of 3 and 5

# def multisum(input_num):
#     multiples = []
#     for num in range(1, input_num + 1):
#         if num % 3 == 0 or num % 5 == 0:
#             multiples.append(num)
    
#     return sum(multiples)

# # These examples should all print True
# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)

# UTF-16 String Value

# def utf16_value(my_string):
#     total = 0

#     for char in my_string:
#         total += ord(char)

#     return total

# # These examples should all print True
# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

# # The next three lines demonstrate that the code
# # works with non-ASCII characters from the UTF-16
# # character set.
# OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
# print(utf16_value(OMEGA) == 937)
# print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)

