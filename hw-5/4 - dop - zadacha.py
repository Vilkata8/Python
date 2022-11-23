def get_collection_builder(col_type):
    if type(col_type) != str:
        return
    if col_type == "tuple":
        def t_build(a, b, c, d):
            l_1 = (a, b, c, d)
            return l_1
        return t_build
    if col_type == "list":
        def l_build(a, b, c, d):
            l_2 = [a, b, c, d]
            return l_2
        return l_build
    if col_type == "set":
        def s_build(a, b, c, d):
            l_3 = {a,b,c,d}
            return l_3
        return s_build

t_build = get_collection_builder("tuple")
t = t_build(1, 2.23, 3, "hi")
l_build = get_collection_builder("list")
c = l_build(12, 6.213, 9, "Harry")
s_build = get_collection_builder("set")
x = s_build(7, 3.23, 11, "hippo")
print("Tuple-ut e:", t)
print("List-ut e:", c)
print("Set-ut e:", x)
