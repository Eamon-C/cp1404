"""
CP1404 prac
wimbledon.py
Estimate: 45min
Actual: 1hour
"""

FILENAME = "wimbledon.csv"


def main():
    data = (get_data())
    champion_to_count, countries = process_data(data)
    display_results(champion_to_count, countries)


def display_results(champion_to_count, countries):
    # displays the results in a formatted fashion
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def process_data(data):
    # adds the desired data into a dictionary
    champion_to_count = {}
    countries = set()
    for line in data:
        countries.add(line[1])
        try:
            champion_to_count[line[2]] += 1
        except KeyError:
            champion_to_count[line[2]] = 1
    return champion_to_count, countries


def get_data():
    # gets the desired information from the wimbledon.csv file
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data


main()
