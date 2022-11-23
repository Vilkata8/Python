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
    
l_1 = [2.2, "+", "/", 9, "+", 2.3, ";"]

print("Sumata e:", sum_list(l_1))

#vuv funkciqta zadavame cikul s usolviq, koito proverqvat ot kakuv tip e dannata, zapisana v spisuka l_1. sled kato otgovori na nqkoe uslovie, vrushta rez -> koeto e rezultatut.