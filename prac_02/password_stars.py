def main():
    length_requirement = 6
    password = get_password(length_requirement)
    print_stars(password)


def print_stars(password):
    print("*" * len(password))


def get_password(length_requirement):
    password = input("Password: ")
    while len(password) < length_requirement:
        print("Insufficient length.")
        password = input("Password: ")
    return password


main()
