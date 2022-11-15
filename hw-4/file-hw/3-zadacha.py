t = input("Vuvedi tekst: ")
d = {}
for i in t:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(f"Rechnikut e: {d}")