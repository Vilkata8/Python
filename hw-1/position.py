num = int(input("Enter your number:"))
bit = int(input("Enter position:"))
print(num & (1<<bit)>0)
