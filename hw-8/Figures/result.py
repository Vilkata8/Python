from Figures import *
print("Triugulnik -> 1 | Romb -> 2 | Trapec -> 3 | Kvadrat -> 4 | Pravougulnik -> 5")
n=input("Vuvedete suotvetniqt znak za suotvetnata figura: ")

if n == "1":
    a = input("Vuvedete strana a: ")
    ha = input("Vuvedete visochinata ha: ")
    triugulnik.triugulnik(a,ha)
elif n == "2":
    a = float(input("Vuvedete strana a: "))
    h = float(input("Vuvedete visochinata h: "))
    Romb.Romb(a, h)
elif n == "3":
    a = float(input("Vuvedete strana a: "))
    b = float(input("Vuvedete strana b: "))
    h = float(input("Vuvedete visochinata h: "))
    trapec.trapec(a, b, h)
elif n == "4":
    a = float(input("Vuvedete stranata a: ")) 
    kvadrat.kvadrat(a)
elif n == "5":
    a = float(input("Vuvedete stranata a: "))
    b = float(input("Vuvedete stranata b: "))
    pravougulnik.pravougulnik(a, b)
else:
    print("Nevaliden znak!")