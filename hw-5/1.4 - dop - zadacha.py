def chisla(n):
    l_1 = []
    for i in range(n):
        num = input(f"Vuvedete element {i+1}: ") 
        if num.isnumeric():
            l_1.append(num)
    return l_1
    
def sum_list(l_2):
    rez = 0
    for i in l_2:
        if type(i) == int:
            rez += i
        elif type(i) == float:
            rez += i
        elif i.isnumeric():
            i = float(i)
            rez += i
    return rez

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


print("Maksimalnata suma ot dvete sumi e:", max_of_two_elements(sum_list(chisla(4)), sum_list(chisla(3))))