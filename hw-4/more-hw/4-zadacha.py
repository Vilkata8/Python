n = int(input("Vuvedi chislo: "))
a = ""
new_n = n
sum_a = 0
for i in range(1, n + 1):
    a += str(n) * i
    if i < n:
        a += ' + '
    sum_a += new_n
    new_n = new_n * 10 + n

print(f"{a} = {sum_a}")