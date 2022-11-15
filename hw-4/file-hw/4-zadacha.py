n = int(input("Vuvedete chislo: "))
l = []
for i in range(1, n):
    l.append(i)
d = {}
for i in l:
    d[i] = l[len(l) - i]

print(f"Spisukut e: {l}")
print(f"Rechnikut e: {d}")