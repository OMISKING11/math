print("Electronic Configuration - ONLY 20")

elements = {"Hydrogen":1, "Helium":2, "Lithium":3, "Beryllium":4, "Boron":5, "Carbon":6, "Nitrogen":7, "oxygen":8, "Fluorine":9, "Neon":10, "Sodium":11, "Magnesium":12, "Aluminium":13, "Silicon":14, "Phosphorus":15, "Sulfur":16, "Chlorine":17, "Argon":18, "Potassium":19, "Calcium":20}

symbol = {"Hydrogen":'H', "Helium":'He', "Lithium":'Li', "Beryllium":'Be', "Boron":'B', "Carbon":'C', "Nitrogen":'N', "Oxygen":'O', "Fluorine":'Fl', "Neon":'Ne', "Sodium":'Na', "Magnesium":'Mg', "Aluminium":'Al', "Silicon":'Si', "Phosphorus":'P', "Sulfur":'S', "Chlorine":'Cl', "Argon":'Ar', "Potassium":'K', "Calcium":'Ca'}
  
en = input("Enter the name of the element: ")
shell = 1
electrons = elements[en]
config = ""

#needs to be fixed
def configuration(element):
  while electrons > 0:
        if electrons >= 2 * shell ** 2:
            config += str(2 * shell ** 2) + ", "
            electrons -= 2 * shell ** 2
        else:
            config += str(electrons) + ", "
            electrons = 0
  print(config)
  
#needs to be fixed

print("Symbol is", symbol[en])
print("Atomic number is", elements[en])
print(electrons)
print("Electronic configuration", configuration(en))
