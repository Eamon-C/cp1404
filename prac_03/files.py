"""
CP1404 - practical
files.py
Several file-reading related codes.
"""

# 1.
name = open('name.txt', 'w')
name.write(input("What is your name? "))
name.close()

# 2.
# in_file = open('name.txt', 'r')
# print("Your name is", in_file.read())
# in_file.close()

# 3.
# in_file = open('numbers.txt', 'r')
# number_1 = int(in_file.readline())
# number_2 = int(in_file.readline())
# in_file.close()
# print(number_1 + number_2)

# 4.
# total = 0
# in_file = open('numbers.txt', 'r')
# numbers = in_file.readlines()
# in_file.close()
# for line in numbers:
#     total += int(line)
# print(total)
