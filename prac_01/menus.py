"""
menus.py
CP1404
A menu that takes a name and responds with three options; "Hello", "Goodbye", "Finished". Includes error checking.
"""

name = input("Name: ")
choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>>").upper()
while choice != "Q":
    if choice == "H":
        (print(f"Hello {name}"))
        choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>>").upper()
    elif choice == "G":
        print(f"Goodbye {name}")
        choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>>").upper()
    else:
        print("Invalid choice")
        choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>>").upper()
print("Finished")

