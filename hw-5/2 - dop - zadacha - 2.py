def sum_list(list):
    result = 0
    for i in list:
        if type(i) == int:
            result += i
        elif type(i) == float:
            result += i
        elif i.isnumeric():
            i = float(i)
            result += i
    return result
    
list_1 = ["a", 12, 3.14, 69, "--", 4, 6]

print("Spisukut e:", list_1)
print("Rezultatut e:", sum_list(list_1))