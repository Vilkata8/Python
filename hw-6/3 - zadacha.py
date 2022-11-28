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

class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university=university
        self.yearofstudy=yearofstudy
    def print(self):
        print(f"Student({self.name}, {self.family}, {self.age}, {self.nationality}, {self.university}, {self.yearofstudy})")

petur=Student("Petur", "Iordanov", 14, "Bulgaria", "TU-Sofia", 3)
petur.print()

class Lecteur(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy, experience):
        super().__init__(name, family, age, nationality)
        self.university=university
        self.yearofstudy=yearofstudy
        self.experience=experience
    def print(self):
        print(f"Student({self.name}, {self.family}, {self.age}, {self.nationality}, {self.university}, {self.yearofstudy} {self.experience})")

petur=Lecteur("Petur", "Iordanov", 14, "Bulgaria", "TU-Sofia", 3, 4) 
petur.print()

