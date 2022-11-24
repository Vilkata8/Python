def digitize(m):
    l_1=[]
    if type(m) == str and m.isnumeric():
        for i in str(m):
            l_1.append(int(i))
        return tuple(l_1)
    	
    else:
        print("Vuveli ste greshen tip danni!")
        return [0,0,0,0]

m=input("Vuvedete chislo: ")

a,b,c,d=digitize(m)
print("A e:",a)
print("B e:",b)
print("C e:",c)
print("D e:",d)
print(a,b,c,d)

# chisloto, koeto vuvejdame e str, zashtoto po tozi nachin edinstveno raboti greshkata za vuveden tekst. Gornata proverka pravi proverka dali chisloto e string i  dali e chislo. Ako e, izpulnqva uslovieto. Kodut raboti, razlikata e, che ne raboti s integer, a sus string.