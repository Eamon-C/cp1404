"""
CP1404 prac, week 7
my_guitars.py
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2022
VINTAGE_YEAR = 50


def main():
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitars.append(Guitar(parts[0], parts[1], parts[2]))

    guitars.sort()

    for guitar in guitars:
        print(guitar)


# my_guitar = Guitar("name", 2000, 100)
# my_guitar_other = Guitar("name", 2001, 100)
# print(my_guitar < my_guitar_other)
main()
