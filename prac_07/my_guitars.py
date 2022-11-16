"""
CP1404 prac, week 7
my_guitars.py
"""

from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    guitars_to_add = []
    get_guitar(guitars_to_add)
    with open(FILENAME, "a") as out_file:
        for guitar in guitars_to_add:
            guitar_string = ",".join(guitar)
            out_file.write("\n" + guitar_string)

    in_file = open(FILENAME, "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitars.append(Guitar(parts[0], parts[1], parts[2]))

    guitars.sort()

    for guitar in guitars:
        print(guitar)


def get_guitar(guitars):
    print("My guitars!")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = input("Year: ")
        cost = input("Cost: ")
        guitars.append([name, year, cost])
        print(f"{name} {year} {cost} added.")
    return guitars


main()
