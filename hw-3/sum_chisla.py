n=int(input("Enter count numbers: "))
sum=0

for i in range(n):
    num=int(input("Enter a number: "))
    sum+=num
    
print(f"The sum is: {sum}")