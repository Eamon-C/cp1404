"""
CP1404 prac,  week 6
guitar_test.py
"""

from prac_06.guitar import Guitar


def main():
    guitar = Guitar("Gibson :-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Another guitar", 2013, 100)
    print(guitar, guitar_2)
    print(guitar.get_age(), guitar_2.get_age())
    print(guitar.is_vintage(), guitar_2.is_vintage())


main()
