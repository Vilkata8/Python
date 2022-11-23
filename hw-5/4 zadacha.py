l_1 = [6, 9, 3, 7, 9, 8, 2, 4, 6, 6]
number = 7

def function(l_2, n_2):
    for i in range(len(l_1)):
        if l_2[i] > n_2:
            l_2[i] = 0
    return l_2

print(function(l_1, number))