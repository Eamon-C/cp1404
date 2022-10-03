"""
CP1404 prac
score_menu.py
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = (float(input("Enter score: ")))
    print(MENU)
    choice = ">".upper()
    while choice != "Q":
        if choice == "G":
            score = (float(input("Enter score: ")))
            result = get_result(score)
        elif choice == "P":
            print_result(result)
        elif choice == "S":


        # temp


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


def print_result(result):
    print(result)


main()
