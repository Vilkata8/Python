import random
l_1 = []
l_2 = []
sum_s = 0
for i in range(5):
    n = random.randint(1, 10)
    l_1.append(n)
l_2.append(l_1[0])
for i in range(len(l_1) - 1):
    sum_s = l_1[i] + l_1[i + 1]
    l_2.append(sum_s)
    l_2.append(l_1[i + 1])

print(f"Purviqt spisuk e: {l_1}")
print(f"Vtoriqt spisuk e: {l_2}")