class InvalidParameterError(Exception):
    pass
class NutrientError(Exception):
    pass
class InvalidFoodError(Exception):
    pass
class Food():
    def __init__(self, name, carbs, protein, fats, salt):
        self.name = name
        self.carbs = float(carbs)
        self.protein = float(protein)
        self.fats = float(fats)
        self.salt = float(salt)
        if type(carbs) != float or type(protein) != float or type(fats) != float or type(salt) != float:
            raise InvalidParameterError
        if carbs > 100 or protein > 100 or fats > 100 or salt > 100:
#if carbs + protein + fats + salt:
#kakvo trqbva da znachi ako nqkoe pole sumata na poletata e poveche ot 100
            raise NutrientError
        if carbs == 0 and protein == 0 and fats == 0 and salt == 0:
            raise InvalidFoodError
    def print_label(self):
        print(f"Food{self.name, self.carbs, self.protein, self.fats, self.salt}")

for i in range(0, 120, 10):
    try:
        chiros = Food("Chiros", 6.12, 2.23, 5.12, 6.54)
    except InvalidParameterError:
        print("InvalidParameterError")
    except NutrientError:
        print("NutrientError")
    except InvalidFoodError:
        print("InvalidFoodError")
    else:
        chiros.print_label()
    finally:
        print("---------------")
#po uslovie ne ni e dadeno finally, no az go slagam, za da si go uprajnq i da razdelq print - ovete na chasti, za po - nagledno
#ot 10 do 13 red gi zapisvame s float, zashtoto taka mojem da vlezem v proverkite dolu
#izpolzvah tozi nachin za pokazvane na kakvahrana stava na vupros. Dobavih si self.name. Ako trqbva, shte go obqsnq v chas.
    