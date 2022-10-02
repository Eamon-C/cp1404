"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A value error occurs when the entered value has a decimal (not an integer) or if the value is simply not a number.
2. When will a ZeroDivisionError occur?
    If the denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    As you cannot divide by 0, adding input checking that asks for a denominator UNTIL a correct value is input would
    avoid the ZeroDivision Error.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:                     #no longer needed
#     print("Cannot divide by zero!")           #no longer needed
print("Finished.")
