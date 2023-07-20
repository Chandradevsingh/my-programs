name = input("Type your name : ")
print("Welcome", name, "to this adventure!")

answer = input("You're on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    print()
elif answer == "right":
    print()
else:
    print("Not a valid option. You loose.")