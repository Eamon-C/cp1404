"""
CP1404 prac
quick_picks.py
"""

import random

NUM_OF_NUMS = 6
MIN_NUM = 1
MAX_NUM = 45

numbers_list = []
quick_picks_list = []
num_quick_picks = int(input("How many quick picks? "))
for i in range(num_quick_picks):
    for j in range(NUM_OF_NUMS):
        number = random.randint(MIN_NUM, MAX_NUM)
        while number in numbers_list:
            number = random.randint(MIN_NUM, MAX_NUM)
        numbers_list.append(number)
    print(" ".join(f"{number:2}" for number in sorted(numbers_list)))
    quick_picks_list.append(numbers_list)
    numbers_list = []
