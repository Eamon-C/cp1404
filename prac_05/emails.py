"""
CP1404 prac
emails.py
Estimate: 30min
Actual: 30min
"""


def main():
    email_to_name = {}
    email = input("email: ")
    while email != "":
        name = derive_name(email)
        response = input(f"Is your name {name}?(Y/n): ").upper()
        if response != "Y" and response != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("email: ")
    print_name_and_email(email_to_name)


def print_name_and_email(email_to_name):
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def derive_name(email):
    email_name = email.split("@")[0]
    full_name = " ".join(email_name.split(".")).title()
    return full_name


main()
