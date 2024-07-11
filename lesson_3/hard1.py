# Question 4

def is_an_ip_number(word):
    if word.isdigit():
        number = int(word)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

a = is_dot_separated_ip_address('4.5.5')
print(a)
b = is_dot_separated_ip_address('1.2.3.4.5')
print(b)
c = is_dot_separated_ip_address('10.4.5.11')
print(c)