def pol(chislo):
    if chislo==chislo[::-1]:
        return 1
    else:
        return 0

n=int(input("Vuvedete chislo: ")) 
      
print(pol(str(n)))