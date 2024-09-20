import random as r 

a = "yes", "y", "yeah", "ye", " ", ""
b = "s", "sh", "", " ", "show"
def ac():
  ask = input("Answer: ")
  print()
  if ask in b:
    print(n)
    cubes()
  ask = int(ask)
  if ask == n:
    print("Bravo!")
  else:
    print("Try again...")
    ac()
    print()


def cubes():
  while True:
    global n
    n = r.randint(1,100)
    print("1   1")
    print("2   8")
    print("3   27")
    print("4   64")
    print("5   125")
    print("6   216")
    print("7   343")
    print("8   512")
    print("9   729")
    cube = n ** 3
    print()
    print("You've to find the cube root of the number given below")
    print()
    print(cube)
    ac()
    again = input("Want a number again: ")
    if again in a:
      cubes()
    else:
      break

cubes()
