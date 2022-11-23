def subirane():
    res=a+b
    return res

def izvajdane():
    res=a-b
    return res
    
def umnojenie():
    res=a*b
    return res
    
def delene():
    res=a/b
    return res

n = input("Vuvedete suotvetniq znak -> |+|-|*|/|: ")

a=float(input("Vuvedete chislo: "))
b=float(input("Vuvedete chislo: "))

if n == "+":
    print("Rezultatut e: ", subirane())
elif n == "-":
    print("Rezultatut e: ", izvajdane())
elif n == "*":
    print("Rezultatut e: ", umnojenie())
elif n == "/":
    print("Rezultatut e: ", delene())
else:
    print("Greshna funkciq.")