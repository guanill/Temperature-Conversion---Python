
def fahtocel(fah):
  return (fah - 32) * 5/9

def fahtokel(fah):
  return (fah - 32) * 5 / 9 + 273.15

def celtofah(cel):
  return cel * (9/5) + 32

def celtokel(cel):
  return cel + 273.15

def keltofah(kel):
  return (kel - 273.15) * 9 / 5 + 32

def keltocel(kel):
  return kel - 273.15
 
#Print final statement
def finalprint(initscale, initdegree, finscale):
    if (initscale == 1 and finscale == 2):
        print(initdegree, "degree Fahrenheit is equal to", fahtocel(initdegree), "degree Celsius.")
    elif (initscale == 1 and finscale == 3):
        print(initdegree, "degree Fahrenheit is equal to", fahtokel(initdegree), "degree Kelvin.")
    elif (initscale == 2 and finscale == 1):
        print(initdegree, "degree Celsius is equal to", celtofah(initdegree), "degree Fahrenheit.")
    elif (initscale == 2 and finscale == 3):
        print(initdegree, "degree Celsius is equal to", celtokel(initdegree), "degree Kelvin.")
    elif (initscale == 3 and finscale == 1):
        print(initdegree, "degree Kelvin is equal to", keltofah(initdegree), "degree Fahrenheit.")
    elif (initscale == 3 and finscale == 2):
        print(initdegree, "degree Kelvin is equal to", keltocel(initdegree), "degree Celsius.")
    elif (initscale == 1 and finscale == 1):
        print(initdegree, "degree Fahrenheit is equal to", initdegree, "degree Fahrenheit.")
    elif (initscale == 2 and finscale == 2):
        print(initdegree, "degree Celsius is equal to", initdegree, "degree Celcius.")
    else:
        print(initdegree, "degree Kelvin is equal to", initdegree, "degree Kelvin.")

#Asks the user the temperature scale and validate it.
def askfirst():
    initscale = int(input("\nSelect the temperature scale: "))
    while(initscale < 1 or initscale > 3):
        initscale = int(input("Invalid option select from 1 to 3: "))
    return initscale

#Asks the user the temperature
def askdegree(initscale):
    if (initscale == 1):
        initdegree = int(input ("You selected Fahrenheit. Enter the degree: "))
    elif (initscale == 2):
        initdegree = int(input ("You selected Celsius. Enter the degree: "))
    else:
        initdegree = int(input ("You selected Kelvin. Enter the degree: "))
    return initdegree

#Asks the user the desired temperature scale and validate it.
def asksecond():
    finscale = int(input("Select the temperature scale you desire to convert to: "))
    while(finscale < 1 or finscale > 3):
        finscale = int(input("Invalid option select from 1 to 3: "))
        
    if (finscale == 1):
        print("You selected Fahrenheit.\n")
    elif (finscale == 2):
        print("You selected Celsius.\n")
    else:
        print("You selected Kelvin.\n")
    
    return finscale

def continu():
    resp = input("\nTry another data? Please use Y or N to answer: ")
    while(not(resp == 'y' or resp == 'Y' or resp == 'n' or resp == 'N')):
        resp = input("Invalid input. Please use Y or N to answer: ")
    return resp

continueto = 'Y'

while(continueto == 'y' or continueto == 'Y'):
    print("\nTEMPERATURE CONVERSION\n1 - Fahrenheit\n2 - Celsius\n3 - Kelvin")
        
    scale1 = askfirst()
    degree = askdegree(scale1)
    scale2 = asksecond()
        
    #Llama a la funcion para imprimir el reporte
    finalprint(scale1, degree, scale2)
        
    #Try other number?
    continueto = continu()
    

print("__________________________________________________")
exit()