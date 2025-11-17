userInput1 = input("Please input your first name: ")
userInput2 = input("Please input your last name: ")
print(f"Your full name is {userInput1} {userInput2}")

# Refactoring using upper and f notation to make some outputs
fullName = f"{userInput1} {userInput2}".upper()
print(f"Your full name is {fullName}")

# Alternative f notation: Format()
print("Your full name is {}".format(fullName))
