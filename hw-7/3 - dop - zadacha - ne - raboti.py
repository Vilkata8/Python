import random
class InvalidParameterError(Exception):
    def __init__(self, message="Invalid class parameter: name", name=""):
        super().__init__(message)
        self.name = name
        #print(message)
#err = InvalidParameterError("Invalid class parameter: Moncho") 
#print(err) 

class InvalidAgeError(InvalidParameterError):
    def __init__(self, message="Invalid parameter: age", age=""):
        super().__init__(message)
        self.age = age
#age = InvalidAgeError("Invalid parameter: 14") 
#print(age) 

class InvalidSoundError(InvalidParameterError):
    def __init__(self, message="Invalid parameter: sound", sound=""):
        super().__init__(message)
        self.sound = sound
#sound = InvalidSoundError("Invalid parameter: Something") 
#print(sound) 

class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
        if type(name) != str:
            raise InvalidParameterError("name")
        if type(age) != int:
            raise InvalidAgeError
        if type(sound) != str:
            raise InvalidSoundError

    def make_sound(self, name, sound):
        print(f"{name} says {sound}!")

    def print(self, name, age, sound):
        pass

    def daily_task(self, animals, name):
        pass
list_1[
            "Iguana", 4, "Maria",
            "Lemur", 4, "Noshko",
            "Snake", 5, "Pincho",
            "Jaguar", 2, "Mishoncho",
        ]

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 15:
            raise InvalidAgeError
        if sound != "r":
            raise InvalidSoundError

    def print(self, name, age, sound):
        print(f"Jaguar({name}, {age}, {sound})")

#    def daily_task(self, l_animals, name):
 #       if "Lemur" or "Human" in list_1:
 #           #list_1.remove("Lemur")
#          print(f"{name} the Jaguar hunted down {animals} the {animal.class__name__}")



#jaguar = Jaguar("Machana", 6, "Rawwr") 
#print(jaguar) 

class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError
        if sound != "e":
            raise InvalidSoundError

    def print(self, name, age, sound):
        print(f"Lemur({name}, {age}, {sound})")

    def daily_task(self, name, fruits):
        self.fruits = fruits
        if fruits >= 10:
            fruits -= 10
            print(f"{name} the Lemur ate a full meal of 10 fruits")
            return fruits
        if fruits < 10:
            fruits -= fruits
            print(f"{name} the Lemur could only find {fruits} fruits")
            return 0
        if fruits <= 0:
            self.make_sound(name, sound)
            self.make_sound(name, sound)
            print(f"{name} the Lemur couldn't find anything to eat")
            return 0

class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError
        if sound != "e":
            raise InvalidSoundError

    def print(self, name, age, sound):
        print(f"Human({name}, {age}, {sound})")

#    def daily_task(self, list_1, l_buildings):
#        pass

#]
#l_buildings[
#          building_1
#          building_2
#          building_3
#]
class Building:
    def __init__(self, type):
        self.type = type

list_2 = [
    "Harry", 3, "hay",
    "Bobo", 5, "seeds",
    "Kolio", 3, "granules",
    "Nonka", 2, "fish"
]

l_buildings = [
    "building_1"
    "building_2"
    "building_3"
]

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

rand = random.randint(1, 10)
for i in range(rand):
    if 1 <= rand <= 3:
        animal = Lemur
    elif 4 <= rand <= 7:
        animal = Jaguar
    else:
        animal = Human
#print(animal)

r_age = random.randint(7, 20)
for age_random in range(r_age):
    pass
#print(age_random)

fruits = 100
animals = list_2[]
buildings = l_buildings[]

for x in range(102):
    animals.append(animal)
    animals.append(r_age)
    animals.append(sounds)

print(f"The jungle now has {len(animals)} animals")
print(animals) 

for anim in animals:
    Lemur.daily_task(Lemur, fruits, 100)
    Jaguar.daily_task(Jaguar, sounds, 20)
    Human.daily_task(names, animals, buildings="")

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
#totalno se oburkah s tazi zadacha. shte moje li da q razgledame v chas?