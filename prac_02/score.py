"""
broken_score.py
CP1404
Program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    print(f"Your result: {get_result(score)}\nRandom result: {get_result(random.randint(0, 100))}")


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score < 50:
            return "bad"
        elif score < 90:
            return "pass"
        else:
            return "excellent"


main()
