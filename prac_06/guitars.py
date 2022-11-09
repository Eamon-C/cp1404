"""
CP1404 prac,  week 6
guitars.py
"""

from prac_06.guitar import Guitar


def get_guitar(guitars):
    pass


def main():
    guitars = []
    print("My guitars!")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40)), guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()
