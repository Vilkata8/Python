num = int(input("Vuvedete broq chisla: "))
l = [int(input("Vuvedete chislo: ")) for x in range(num)]
num_2 = int(input("Vuvedi nomer na operaciqta(0,1): "))
if num_2 == 0:
    for i in range(len(l)):
        if i % 2 == 0 & i != 0:
            l[i] += 5
    else:
        for i in range(len(l)):
            if i % 2 != 0:
                l[i] += 10

print(l)