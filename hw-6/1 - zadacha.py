class Person:
    def __init__(self, name, family, age, nationality):
        self.name=name
        self.family=family
        self.age=age
        self.nationality=nationality
alex=Person("Alex", "Iordanov", 18, "Bulgaria")
ivan=Person("Ivan", "Iordanov", 16, "Bulgaria")
petur=Person("Petur", "Iordanov", 14, "Bulgaria")

l=[]
l.append(alex)
l.append(ivan)
l.append(petur)
print(l)