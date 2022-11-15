n = input("Vuvedete chislo: ")
t_1 = tuple(n)
n_1 = int(n[::-1])
t_2 = tuple(str(n_1))

print(f"Purviqt kortej e: {t_1}")
print(f"Vtoriqt kortej e: {t_2}")