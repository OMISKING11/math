def ask():
  print("1 for Compound Interest")
  print("2 for Principal")
  print("3 for Rate of interest")
  print("4 for Time")
  global value, principal, amount, roi, time, ci
  value = int(input("Which element's value you want: "))
  if value == 1:
    principal = float(input("Principal: "))
    roi = float(input("Rate of Interest: "))
    time = float(input("Time: "))
    amount = principal * (1 + roi / 100)**time
    ci = amount - principal
    print("Principal is:", principal)
    print("Rate of Interest is:", roi)
    print("Time is:", time)
    print("Formula for taking out compound Interest is \n"
          "P(1 + roi/100) ** time")
    print(
        "ci =",
        principal,
        "*",
        roi,
        "*",
        time,
        "/ 100",
    )
    print("ci =", ci)
    print("Amount =", amount)
  if value == 2:
    ci = float(input("Compound Interest: "))
    roi = float(input("Rate of Interest: "))
    time = float(input("Time: "))
    principal = amount / ( 1 + roi / 100) ** time
    amount = principal + ci
    print("Rate of Interest is:", roi)
    print("Time is:", time)
    print("Compound Interest is:", ci)
    print("Formula for taking out Principal is \n"
          " P = amount / ( 1 + roi / 100) ** time")
    print("P =", amount, "/", "( 1 +", roi, "/100) **", time)
    print("P =", principal)
    print("Amount =", amount)
  if value == 3:
    ci = float(input("Compound Interest: "))
    principal = float(input("Principal: "))
    time = int(input("Time: "))
    amount = float(input("Amount: "))
    roi = 100 * ((amount / principal)**1 / time - 1)

    print("Principal is:", roi)
    print("Time is:", time)
    print("Compound Interest is:", ci)
    print("Formula for taking out Rate of Interest is \n"
          "Rate of Interest = 100*((amount/principal) ** 1/time - 1)")
    print("Rate of Interest =", "100*((", amount, "/", principal, ") ** 1/",
          time, " - 1)")
    print("Rate of Interest=", roi)
    print("Amount =", amount)
  if value == 4:
    ci = int(input("compound Interest: "))
    principal = int(input("Principal: "))
    roi = int(input("Rate of Interest: "))
    time = ci * 100 / principal * roi
    amount = principal + ci
    print("Rate of Interest is:", roi)
    print("Principal is: ", principal)
    print("compound Interest is:", ci)
    print("Formula for taking out Rate of Interest is \n"
          "T = ci * 100 / P * Rate of Interest")
    print("Time =", ci, "* 100", "/", principal, "*", roi)
    print("Time =", time)
    print("Amount =", amount)
  again()


def again():
  ready = ("y", "yes", "ye", "y ", " y", "ye ", "yes ")
  wpa = input("Wanna play again y/n: ")
  if wpa in ready:
    ask()
  else:
    print("Thank you for playing my game ")
    pass


if __name__ == "__main__":
  ask()
