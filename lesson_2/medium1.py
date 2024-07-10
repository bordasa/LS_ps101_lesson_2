# Question 1
# string = 'The Flintstones Rock!'

# for num in range(1, 11):
#     print(num * '-' + string)

# Question 2
# def factors(number):
#     divisor = number
#     result = []
#     while divisor > 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

# print(factors(10))
# print(factors(-10))

# Question 3
# def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
#     buffer = buffer + [new_element]
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer
# def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
#     buffer.append(new_element)
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# my_string = ['-', '-', '-', '-']
# print(add_to_rolling_buffer1(my_string, 4, '='))
# print(add_to_rolling_buffer1(my_string, 3, '='))
# print(add_to_rolling_buffer1(my_string, 2, '='))
# print(add_to_rolling_buffer1(my_string, 5, '='))
# print(add_to_rolling_buffer1(my_string, 6, '='))

