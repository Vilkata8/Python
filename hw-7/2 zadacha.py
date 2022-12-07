import math
try:
    n = int(input("Vuvedete chislo: "))
    print("Korenut mu e:", math.sqrt(n))
except ValueError:
    print("Invalid Number!")
finally:
    print("Good Bye!")