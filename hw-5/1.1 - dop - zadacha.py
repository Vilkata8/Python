def chisla(n):
    l_1 = []
    for i in range(n):
        num = input(f"Vuvedete element {i+1}: ") 
        if num.isnumeric():
            l_1.append(num)
    return l_1
    
counter = int(input("Vuvedete broq elementi: "))

print(chisla(counter))

# 4 red - tova v {} i+1 oznachava chisloto, koeto se pokazva na vsqko izpulnenie na cikula s vuvejdaneto na chsilata da se uvelichi s 1=> to se vzima ot broq puti izpulnenie na cikula. Tova f otpred se slaga, za da se izpulni iteraciqta v skobite. 
# 5 red - tova .isnumeric vzima chislata ot num, koito sme vuveli. 
# 6 red - tova .append dobavq chislata ot num v l_1