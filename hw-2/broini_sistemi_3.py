import string
base=string.digits + string.ascii_letters
a=int(input('Input number: '))
b=int(input('Input base: '))
result=''
while a//b !=0:
    result += base[a%b]
    a//=b
print(1,result[::-1])
#imam vupros otnosno tova na 11 red
