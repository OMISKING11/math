print("!!!Welcome to GAIN, LOSS, SP and CP percent remover!!!")
print("1 for gain or profit percent")
print("2 for loss percent")
print("3 for SP percent")
print("4 for CP percent")

def gain():
  profit = float(input("what is the profit: "))
  cp = float(input("What is the cp: "))
  percent = profit/cp * 100
  print("The profit percent is", percent)

def loss():
  loss = float(input("What is the loss: "))
  cp = float(input("What is the cp: "))
  percent = loss/cp * 100
  print("The loss percent is", percent)

def sp():
  p_o_l = input("Is the sp in profit(y) or loss(n): ")
  p_o_lp = float(input("What is the percent of gain or loss: "))
  cp = float(input("What is the cp: "))
  if p_o_l == "y":
    percent = (100 + p_o_lp)/100 *  cp
  else:
    percent = (100 - p_o_lp)/100 * cp
  print("The SP percent is", percent)

def cp():
  p_o_l = input("Is the cp in profit(y) or loss(n): ")
  p_o_lp = float(input("What is the percent of gain or loss: "))
  sp = float(input("What is the SP: "))
  if p_o_l == "y":
    percent = 100 / (100 + p_o_lp) * sp
  else:
    percent = 100 / (100 - p_o_lp) * sp
  print("The SP percent is", percent)

while True:
  ask = int(input("Which value do you want to find out: "))
  if ask == 1:
    gain()
  elif ask == 2:
    loss()
  elif ask == 3:
    sp()
  elif ask == 4:
    cp()
  else:
    break
