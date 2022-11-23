a = []
def list_avg(lst):
    b = []
    counter = int(input("Vuvedete broq elementi: "))
    suma = 0
    for i in range(counter):
        n_in = input(f"Vuvedete element {i+1}: ")
        lst.append(n_in)
        if n_in.isnumeric() or n_in.isdigit():
            b.append(n_in)
            suma += float(n_in)
        aver_1 = suma / len(b)
    print("Spisuk:", b)
    return aver_1

print("Srednoaritmetichnoto na dvete chisla e:", list_avg(a))
# metodi za dobavqne 