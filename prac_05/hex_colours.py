"""
CP1404 prac
hex_colours.py
"""

name_to_code = {'Absolute Zero': '#0048ba', 'Acid Green': '#b0bf1a', 'Alizarin crimson': '#e32636',
                'Black': '#000000', 'Canary': '#ffff99', 'Cyclamen': '#f56fa1', 'Daffodil': '#ffff31',
                'DarkKhaki': '#bdb76b', 'Glossy Grape': '#ab92b3'}

max_len = len(max(name for name in name_to_code))

for colour_name, colour_code in name_to_code.items():
    print(f"{colour_name:>{max_len}} is {colour_code}")

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", name_to_code[colour_name])
    except KeyError:
        print("Invalid input!")
    colour_name = input("Enter colour name: ").title()
