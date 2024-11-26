import math

def Final_Velocity():
    scheck = int(input("Enter 1 if you have distance, 2 if you have time: "))
    if scheck == 1:
        s = float(input("Enter the distance: "))
        u = float(input("Enter the initial velocity: "))
        ucheck = int(input("Is the initial velocity in m/s(1) or km/h(2): "))
        if ucheck == 2:
            u = u * 5/18
        a = float(input("Enter the acceleration: "))
        acheck = int(input("Is the acceleration in m/s^2(1) or km/h^2(2): "))
        if acheck == 2:
            a = a * 5/18
        v = math.sqrt(u**2 + 2*a*s)
        print("The formula is v² = u² + 2as")
        print("The final velocity is", v, "m/s")

    elif scheck == 2:
        u = float(input("Enter the initial velocity: "))
        ucheck = int(input("Is the initial velocity in m/s(1) or km/h(2): "))
        if ucheck == 2:
            u = u * 5/18
        a = float(input("Enter the acceleration: "))
        t = float(input("Enter the time: "))
        v = u + a * t
        answer = int(input("You want the answer in m/s(1) or km/h(2): "))
        if answer == 1:
            print("The formula is v² = u² + 2as")
            print("The final velocity is", v, "m/s")
        else:
            v = v * 18/5
            print("The formula is v = u + at")
            print("The final velocity is", v, "km/hr")

def Initial_Velocity():
    v = float(input("Enter the final velocity: "))
    vcheck = int(input("Is the final velocity given in m/s(1) or km/h(2): "))
    if vcheck == 2:
        v = v * 5/18
    a = float(input("Enter the acceleration: "))
    t = float(input("Enter the time: "))
    u = v - a * t
    answer = int(input("You want the answer in m/s(1) or km/h(2): "))
    if answer == 1:
        print("The formula is v = u + at")
        print("The initial velocity is", u, "m/s")
    else:
        u = u * 18/5
        print("The formula is v = u + at")
        print("The initial velocity is", u, "km/hr")

def Acceleration():
    scheck = int(input("Is the distance and time(1), the v and time(2), the force(3), distance and v and u(4): "))
    if scheck == 1:
        d = float(input("Enter the distance in m: "))
        u = float(input("Enter the initial velocity in m/s: "))
        t = float(input("Enter the time in s: "))
        a = (2 * (d - u * t)) / t ** 2
        print("The formula is v² = u² + 2as")
        print("The acceleration is", a, "m/s^2")
    elif scheck == 2:
        v = float(input("Enter the final velocity: "))
        vcheck = int(input("Is the final velocity given in m/s(1) or km/h(2): "))
        if vcheck == 2:
            v = v * 5/18
        u = float(input("Enter the initial velocity: "))
        ucheck = int(input("Is the initial velocity in m/s(1) or km/h(2): "))
        if ucheck == 2:
            u = u * 5/18
        t = float(input("Enter the time: "))
        a = (v - u) / t
        answer = int(input("You want the answer in m/s^2(1) or km/h^2(2): "))
        if answer == 1:
            print("The formula is v = u + at")
            print("The acceleration is", a, "m/s^2")
        else:
            a = a * 18/5
            print("The formula is v = u + at")
            print("The acceleration is", a, "km/hr^2")
    elif scheck == 3:
        f = float(input("Enter the force: "))
        m = int(input("Enter the mass in kg: "))
        a = f / m
        answer = int(input("You want the answer in m/s^2(1) or km/h^2(2): "))
        if answer == 1:
            print("The formula is F = ma")
            print("The acceleration is", a, "m/s^2")
        else:
            a = a * 18/5
            print("The formula is F = ma")
            print("The acceleration is", a, "km/hr^2")
    elif scheck == 4:
        d = float(input("Enter the distance in m: "))
        v = float(input("Enter the final velocity in m/s: "))
        u = float(input("Enter the initial velocity in m/s: "))
        a = ((v ** 2) - (u ** 2)) / (2 * d)
        print("The formula is v² = u² + 2as")
        print("The acceleration is", a, "m/s^2")
        

def Time():
    ask1 = int(input("Do you have distance? Enter 1 for Yes, 2 for No: "))
    if ask1 == 1:
        d = float(input("Enter the distance: "))
        dcheck = int(input("Is the distance given in m(1) or km(2): "))
        if dcheck == 2:
            d = d * 1000
        u = float(input("Enter the initial velocity: "))
        ucheck = int(input("Is the initial velocity in m/s(1) or km/h(2): "))
        if ucheck == 2:
            u = u * 5/18
        a = float(input("Enter the acceleration: "))
        discriminant = u**2 + 2 * a * d

        if discriminant < 0:
            print("No real solution for t, as the discriminant is negative.")
        else:
            t1 = (-u + math.sqrt(discriminant)) / a
            t2 = (-u - math.sqrt(discriminant)) / a
            print("The formula is s = ut + 0.5at²")
            print("The possible values of time are", t1, t2, "seconds")
    else:
        v = float(input("Enter the final velocity: "))
        vcheck = int(input("Is the final velocity in m/s(1) or km/h(2): "))
        if vcheck == 2:
            v = v * 5/18
        u = float(input("Enter the initial velocity: "))
        ucheck = int(input("Is the initial velocity in m/s(1) or km/h(2): "))
        if ucheck == 2:
            u = u * 5/18
        a = float(input("Enter the acceleration: "))
        t = (v - u) / a
        print("The formula is v = u + at")
        print("The time is", t, "seconds")

def Distance():
    u = float(input("Enter the initial velocity: "))
    ucheck = int(input("Is the initial velocity in m/s(1) or km/h(2): "))
    if ucheck == 2:
        u = u * 5/18
    a = float(input("Enter the acceleration: "))
    t = float(input("Enter the time: "))
    d = (u * t) + (0.5 * a * t * t)
    print("The formula is s = ut + 0.5at²")
    print("The distance is", d, "meters")

while True:
    print()
    print("This program calculates the motion of any object. Just fill in the correct values and you are good to go.")
    print("Made by Om Kumar")
    print("Which value do you want to find out?\n"
          "1. Final Velocity\n"
          "2. Initial Velocity\n"
          "3. Acceleration\n"
          "4. Time\n"
          "5. Distance")
    ask = int(input("Enter the number of the value you want to find out: "))
    if ask == 1:
        Final_Velocity()
    elif ask == 2:
        Initial_Velocity()
    elif ask == 3:
        Acceleration()
    elif ask == 4:
        Time()
    elif ask == 5:
        Distance()
    else:
        break