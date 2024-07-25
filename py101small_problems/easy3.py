# Repeat Yourself

# def repeat(string, num):
#     for _ in range(num):
#         print(string)

# repeat('Hello', 3)
# repeat('I love my flower', 50)
# repeat('Miami', 0)

# ddaaiillyy ddoouubbllee

# def crunch(string):
#     new_string = ""

#     if len(string) > 0:
#         new_string = string[0]

#         for char in string:
#             if new_string[-1] != char:
#                 new_string += char
    
#     return new_string

# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('gggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

# Bannerizer

# def print_in_box(string):
#     print('+-' + ('-' * len(string)) + '-+')
#     print('| ' + (' ' * len(string)) + ' |')
#     print('| ' + string + ' |')
#     print('| ' + (' ' * len(string)) + ' |')
#     print('+-' + ('-' * len(string)) + '-+')

# print_in_box('To boldly go where no one has gone before.')
# print_in_box('I am lucky to have my boo!')
# print_in_box('')

# Strings Strings

# def stringy(length):
#     result = ''
#     for num in range(length):
#         if num % 2 == 0:
#             result += '1'
#         else:
#             result += '0'
    
#     return result

# print(stringy(6) == '101010')
# print(stringy(9) == '101010101')
# print(stringy(4) == '1010')
# print(stringy(7) == '1010101')

# Right Triangles

# def triangle(num):
#     iterator = 1

#     while num > 0:
#         triangle_string = ' ' * (num - 1) + '*' * iterator
#         print(triangle_string)
#         num -= 1
#         iterator += 1

# triangle(5)
# triangle(9)

# Madlibs

# noun = input('Enter a noun: ')
# verb = input('Enter a verb: ')
# adj = input('Enter an adjective: ')
# adverb = input('Enter an adverb: ')
# print()
# print(f"Do you {verb} your {adj} {noun} {adverb}? That's hilarious!")
# print(f"The {adj} dog {verb}s {adverb} over the lazy {noun}.")
# print(f"The {noun} {adverb} {verb}s up to Joe's {adj} turtle.")

# Double Doubles

# def twice(number):
#     num_string = str(number)
#     middle = len(num_string) // 2

#     if num_string[: middle] == num_string[middle :]:
#         return number
    
#     else:
#         return number * 2

# print(twice(37) == 74)
# print(twice(44) == 44)
# print(twice(334433) == 668866)
# print(twice(444) == 888)
# print(twice(107) == 214)
# print(twice(103103) == 103103)
# print(twice(3333) == 3333)
# print(twice(7676) == 7676)

# Grade Book

# def get_grade(score1, score2, score3):
#     average_score = (score1 + score2 + score3) / 3

#     if average_score >= 90:
#         return 'A'
#     elif average_score >= 80:
#         return 'B'
#     elif average_score >= 70:
#         return 'C'
#     elif average_score >= 60:
#         return 'D'
#     else:
#         return 'F'

# print(get_grade(95, 90, 93) == 'A')
# print(get_grade(50, 50, 95) == 'D')

###########################################
# Clean up the words

def clean_up(string):

    new_string = ''

    for index, element in enumerate(string):
        if element.isalpha():
            new_string += element
        
        else:
            if index == 0 or string[index - 1].isalpha():
                new_string += ' '
    
    return new_string

print(clean_up("---what's my +*& line?") == " what s my line ")

##############################################

# What Century is That?

# def century(year):
#     hundreds = year // 100
#     tens = year % 100
    
#     if tens > 0:
#         hundreds += 1
    
#     cent = str(hundreds)

#     if cent[-1] == '1' and hundreds % 100 != 11:
#         cent += 'st'
#     elif cent[-1] == '2' and hundreds % 100 != 12:
#         cent += 'nd'
#     elif cent[-1] == '3' and hundreds % 100 != 13:
#         cent += 'rd'
#     else:
#         cent += 'th'
    
#     return cent

# print(century(2000) == '20th')
# print(century(2001) == '21st')
# print(century(1965) == '20th')
# print(century(256) == '3rd')
# print(century(5) == '1st')
# print(century(10103) == '102nd')
# print(century(1052) == '11th')
# print(century(1127) == '12th')
# print(century(11201) == '113th')