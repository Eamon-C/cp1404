length_requirement = 6
password = input("Password: ")
while len(password) < length_requirement:
    print("Insufficient length.")
    password = input("Password: ")
print("*" * len(password))
