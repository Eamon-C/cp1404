"""
CP1404 prac
score_menu.py
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = get_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print(print_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_score():
    score = int(input("score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("score: "))
    return score


def print_result(score):
    if score < 50:
        return "bad"
    elif score < 90:
        return "pass"
    else:
        return "excellent"


def print_stars(score):
    print("*" * score)


main()
