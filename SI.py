def ask():
  print("1 for Simple Interest")
  print("2 for Principal")
  print("3 for Rate of interest")
  print("4 for Time")
  global value, principal, amount, roi, time, si
  value = int(input("Which element's value you want: "))
  if value == 1:
    principal = float(input("Principal: "))
    roi = float(input("Rate of Interest: "))
    time = float(input("Time: "))
    si = principal * roi * time / 100
    amount = principal + si
    print("Principal is:", principal)
    print("Rate of Interest is:", roi)
    print("Time is:", time)
    print("Formula for taking out Simple Interest is \n"
         "SI = P * R * T / 100")
    print("SI =", principal, "*", roi, "*", time, "/ 100", )
    print("SI =", si)
    print("Amount =", amount)
  if value == 2:
    si = float(input("Simple Interest: "))
    roi =float(input("Rate of Interest: "))
    time = float(input("Time: "))
    principal = si * 100 / roi * time
    amount = principal + si
    print("Rate of Interest is:", roi)
    print("Time is:", time)
    print("Simple Interest is:", si)
    print("Formula for taking out Principal is \n"
         "P = I * 100 / R * T")
    print("P =", si, "* 100", "/", roi, "*", time)
    print("P =", principal)
    print("Amount =", amount)
  if value == 3:
    si = int(input("Simple Interest: "))
    principal = int(input("Principal: "))
    time = int(input("Time: "))
    roi = si * 100 / principal * time
    amount = principal + si
    print("Principal is:", roi)
    print("Time is:", time)
    print("Simple Interest is:", si)
    print("Formula for taking out Rate of Interest is \n"
         "Rate of Interest = SI * 100 / P * T")
    print("Rate of Interest =", si, "* 100", "/", principal, "*", time)
    print("Rate of Interest=", roi)
    print("Amount =", amount)
  if value == 4:
    si = int(input("Simple Interest: "))
    principal = int(input("Principal: "))
    roi = int(input("Rate of Interest: "))
    time = si * 100 / principal * roi
    amount = principal + si
    print("Rate of Interest is:", roi)
    print("Principal is: ", principal)
    print("Simple Interest is:", si)
    print("Formula for taking out Rate of Interest is \n"
         "T = SI * 100 / P * Rate of Interest")
    print("Time =", si, "* 100", "/", principal, "*", roi)
    print("Time =", time)
    print("Amount =", amount)
  again()
  
def again():
  ready = ("y", "yes", "ye", "y ", " y", "ye ", "yes ")
  wpa= input("Wanna play again y/n: ")
  if wpa in ready:
    ask()
  else:
    print("Thank you for playing my game ")
    pass
if __name__ == "__main__":
  ask()
    
    
