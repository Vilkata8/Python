num=27102022
devisor=16
result=""
while num>0:
    remainder=num%16
    if remainder==10:
        result+='A'
    elif remainder==11:
        result+='B'
    elif remainder==12:
        result+='C'
    elif remainder==13:
        result+='d'
    elif remainder==14:
        result+='E'
    elif remainder==15:
        result+='F'
    else:
        result+=str(remainder)
    num//16
print(result[::-1])