from math import *


def perimeter():
  print(
    "Type 1 for square, 2 for rectangle or parallelogram, 3 for circle, 4 for triangle"
  )
  n = int(input("Type here"))
  if n == 1:
    side = float(input("Enter the side: "))
    perimeter = 4 * side
    print("The perimeter is", perimeter)
  elif n == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    perimeter = 2 * (l + b)
    print("The perimeter is", perimeter)
  elif n == 3:
    r = float(input("Enter the radius: "))
    c = 2 * 22 / 7 * r
    print("The circumference is", c)
  elif n == 4:
    print(
      "Type 1 for equilateral triangle, 2 for isosceles triangle, 3 for scalene triangle"
    )
    o = int(input("Type here: "))
    if o == 1:
      side = float(input("Enter the side of the triangle: "))
      perimeter = 3 * side
      print("The perimeter is", perimeter)
    elif o == 2:
      eside = float(input("Enter the value of the equal sides: "))
      side1 = float(input("Enter the left side: "))
      perimeter = eside * 2 + side1
      print("The perimeter is", perimeter)
    elif o == 3:
      side1 = float(input("Enter first side: "))
      side2 = float(input("Enter second side: "))
      side3 = float(input("Enter third side: "))
      perimeter = side1 + side2 + side3
  else:
    pass


def area():
  print(
    "Type 1 for square, 2 for rectangle or parallelogram, 3 for circle, 4 for triangle"
  )
  n = int(input("Type here: "))
  if n == 1:
    side = float(input("Enter the side: "))
    area = side * side
    print("The area is", area)
  elif n == 2:
    l = float(input("Enter the length or height(altitude): "))
    b = float(input("Enter the breadth or base: "))
    area = l * b
    print("The area is", area)
  elif n == 3:
    r = float(input("Enter the radius: "))
    area = 22 / 7 * r * r
    print("The area is", area)
  elif n == 4:
    b = float(input("Enter the base of triangle: "))
    h = float(input("Enter the height of the triangle: "))
    area = 1 / 2 * b * h
    print("The area is", area)
  else:
    pass


def radius():
  print("Type 1 if to be found from area and 2 if circumference")
  p = int(input("Type here: "))
  if p == 1:
    area = float(input("Enter area: "))
    radius = sqrt(area * 7 / 22)
    print("The radius is", radius)
  if p == 2:
    c = float(input("Enter circumference: "))
    radius = c / 1 / 2 * 7 / 22
    print("The radius is", radius)


while True:
  print(
    "Type 1 for area and 2 for circumference or perimeter 3 for radius of cirlce any No. to exit"
  )
  i = int(input("Type here: "))
  if i == 1:
    area()
  elif i == 2:
    perimeter()
  elif i == 3:
    radius()
  else:
    break
