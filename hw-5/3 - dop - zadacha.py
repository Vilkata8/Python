def digitize(m):
    l_1=[]
    for i in str(m):
        l_1.append(int(i))
    return tuple(l_1)
m=int(input("Vuvedete chislo: "))

if type(m) != int:
    print("Vuveli ste greshen tip danni!")

a,b,c,d=digitize(m)
print("A e:",a)
print("B e:",b)
print("C e:",c)
print("D e:",d)
print(a,b,c,d)
#imam problem s greshkata, koqto da izvede, ako ne e vuvedeno integer 