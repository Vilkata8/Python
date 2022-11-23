def is_valid_triangle(a,b,c):
    if a < b + c and b < a + c and c < a + b:
        return "Vuzmojen triugulnik!" #True
    else:
        return "Nevuzmojen triugulnik!" #False

a = float(input("Vuvedete stranata a: "))
b = float(input("Vuvedete stranata b: "))
c = float(input("Vuvedete stranata c: "))

triangle = is_valid_triangle
print("Otgovor:", triangle(a,b,c))