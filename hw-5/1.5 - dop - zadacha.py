def sum_list(l_2):
    rez = 0
    for i in l_2:
        if type(i) == int:
            rez += i
        elif type(i) == float:
            rez += i
        elif i.isnumeric():
           i = float(i)
           rez == i
    return rez
    
def max_of_two_elements(n, m):
    if str(n).replace(".", "").isnumeric() and str(m).replace(".", "").isnumeric():
       if float(n) >= float(m):
            return n
       else:
            return m
    
print("Maksimalnoto ot chislata e:", max_of_two_elements(sum_list([4, "AA@", 3.12, "1"]), "9.2"))
# imam vupros otnosno funkciqta max_fo_two_elements, koito shte vi zadam v chasa. Ot predishnite zadachi moqta funkciq ne raboteshe zarad problem s edni chovki i ne uspqh da go opravq. tova e raboteshta funkciq ot edin kolega, koito pomolih. i mi pozvoli da go polzvam.