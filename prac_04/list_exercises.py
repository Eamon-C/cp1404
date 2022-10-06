"""
CP1404 prac
list_exercises
"""

# NUMBER_OF_NUMBERS = 5
# numbers = []
# for i in range(NUMBER_OF_NUMBERS):
#     numbers.append((int(input("Number: "))))
# print(f"The first number is {numbers[0]}")
# print(f"The last number is {numbers[-1]}")
# print(f"The smallest number is {min(numbers)}")
# print(f"The largest number is {max(numbers)}")
# print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_input = input("username: ")
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")
