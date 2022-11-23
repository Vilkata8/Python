def kvadrat():
    a=float(input("Vuvedete stranata a: "))
    res=a*a
    return res

def pravougulnik():
    a=float(input("Vuvedete stranata a: "))
    b=float(input("Vuvedete stranata b: "))
    res=a*b
    return res
    
def triugulnk():
    a=float(input("Vuvedete stranata a: "))
    b=float(input("Vuvedete stranata b: "))
    res=(a*b)/2
    return res

figure = input("Vuvedete vida figura - kvadrat/pravougulnik/triugulnik: ")

if figure == "kvadrat":
    kvadrat()
elif figure == "pravougulnik":
    pravougulnik()
elif figure == "triugulnik":
    triugulnk()
else:
    print("Ne ste vuveli figura. ")