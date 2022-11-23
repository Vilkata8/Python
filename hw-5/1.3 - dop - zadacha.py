def max_of_two_elements(n_1, n_2):
    if type(n_1) == str() and type(n_2) != str():
        return b
    elif type(n_2) == str() and type(n_1) != str():
        return a
    elif type(n_1) == str() and type(n_2) == str():
        return
    elif n_1 > n_2:
        return n_1
    elif n_1 < n_2:
        return n_2
    elif n_1 == n_2:
        return n_1

n_1 = input("Vuvedete chislo 1: ")
n_2 = input("Vuvedete chislo 2: ")

print("Maksimalnoto ot dvete chisla e:", max_of_two_elements(n_1, n_2))