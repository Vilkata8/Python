n = int(input("Vuvedi chisloto n: "))
d_1 = dict()

for x in range(n):
    key = input("Vuvedi kluch: ")
    value = input("Vuvedi stoinost: ")
    d_1[key] = value
m = int(input("Vuvedi broq na stoinostite m: "))
m_1 = [input("Vuvedete klucha: ") for x in range(m)]
for x in list(d_1):
    for y in range(len(m_1)):
        if x == m_1[y]:
            m_1[y] = d_1[x]
            del d_1[x]

print(f"Rechnikut e: {d_1}")
print(f"Spisukut e: {m_1}")