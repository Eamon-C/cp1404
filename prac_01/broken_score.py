"""
broken_score.py
CP1404
Program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score < 50:
        print("bad")
    elif score < 90:
        print("pass")
    else:
        print("excellent")
