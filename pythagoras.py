import math as m

i = ("y", "yes", "ye", "yes ")
def ask():
    print()
    print("The Pythagoras Theorem")
    print("type 1 for Hypotenuse")
    print("type 2 for Perpendicular")
    print("type 3 for Base")
    print("In our case c² is Hypotenuse, a² is Perpendicular and b² is Base")
    global choice
    choice = int(input("what do you want to find out in pythagoras theorem? "))


def hypotenuse():
    b = float(input("Base is: "))
    a = float(input("Perpendicular is: "))
    # taking out the squares
    a2 = a ** 2
    b2 = b ** 2
    # adding them
    ans = a2 + b2
    ans1 = m.sqrt(ans)
    # printing formula
    print("Formula for Hypotenuse is a² + b² = c²")
    # both the squares
    print(a, "square is", a2)
    print(b, "square is", b2)
    # their sum
    print("Now their sum is", ans)
    # final answer
    print("So, Hypotenuse =", ans)
    print("Hypotenuse =", ans1)


def perpendicular():
        # taking integer input
    c = float(input("Hypotenuse is: "))
    b = float(input("Base is: "))
    # taking out squares
    c2 = c ** 2
    b2 = b ** 2
    # subtracting them
    ans = c2 - b2
    ans1 = m.sqrt(ans)
    # printing formula
    print("Formula for Perpendicular is c² - b² = a²")
    # both the squares
    print(c, "square is", c2)
    print(b, "square is", b2)
    # their difference
    print("Now their difference is", ans)
    # final answer
    print("So, Perpendicular =", ans)
    print("Perpendicular =", ans1)


def base():
    c = float(input("Hypotenuse is: "))
    a = float(input("Perpendicular is: "))
    # taking out squares
    c2 = c ** 2
    a2 = a ** 2
    # subtracting them
    ans = c2 - a2
    ans1 = m.sqrt(ans)
    # printing formula
    print("Formula for Base is c² - a² = b²")
    # both the squares
    print(c, "square is", c2)
    print(a, "square is", a2)
    # their difference
    print("Now their difference is", ans)
    # final answer
    print("Base =", ans)
    print("Base =", ans1)


while True:
    ask()
    # checking which function to run
    if choice == 1:
        # 1 is for hypotenuse
        hypotenuse()
        ask()
    if choice == 2:
        perpendicular()
        # 2 is for perpendicular
        ask()
    if choice == 3:
        base()
        # 3 is for base
        ask()
    if choice == "bye" or "bye ":
        break
    else:
        # if no input matches then try again
        print("Try again ")
        ask()
