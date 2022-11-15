n = int(input("Vuvedete chislo: "))
a = 0
b = 1
for i in range(0, n + 2):
    print(a, end=",")
    a, b = b, a + b