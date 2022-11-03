num=27102022
devisor=2
result=""
while num//2>0:
    result+=str(num%2)
    num//2
print(result[::-1])
