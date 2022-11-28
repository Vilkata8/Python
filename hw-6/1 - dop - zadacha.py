class Vehicle:
    def __init__(self, brand, model, engine_volume, maximum_speed, total_km, max_passengers):
        self.brand = brand
        self.model = model
        self.engine_volume = engine_volume
        self.maximum_speed = maximum_speed
        self.total_km = total_km
        self.max_passengers = max_passengers
    def print_info(self):
        print(f"Vehicle: {self.brand}, {self.model}, {self.engine_volume}, {self.maximum_speed}, {self.total_km}, {self.max_passengers}")
        
class Motorbike(Vehicle):
    def __init__(self, brand, model, engine_volume, maximum_speed, total_km, price, has_basket):
        super().__init__(brand, model, engine_volume, maximum_speed, total_km, 2)
        self.price = price
        self.has_basket = has_basket
    def print_info(self):
        print(f"Motorbike: {self.brand}, {self.model}, {self.engine_volume}, {self.maximum_speed}, {self.max_passengers}, {self.total_km}, {self.price}, {self.has_basket}")

#category, fuel_type -> str
class Car(Vehicle):
    def __init__(self, brand, model, engine_volume, maximum_speed, total_km, category, fuel_type):
        super().__init__(brand, model, engine_volume, maximum_speed, total_km, 4)
        self.category = category
        self.fuel_type = fuel_type
    def print_info(self):
        print(f"Car: {self.brand}, {self.model}, {self.engine_volume}, {self.maximum_speed}, {self.total_km}, {self.max_passengers}, {self.category}, {self.fuel_type}")


class Bus(Vehicle):
    def __init__(self, brand, model, engine_volume, maximum_speed, total_km, max_passengers, firm, year_production):
        super().__init__(brand, model, engine_volume, maximum_speed, total_km, max_passengers)
        self.firm = firm
        self.year_production = year_production
    def print_info(self):
        print(f"Bus: {self.brand}, {self.model}, {self.engine_volume}, {self.maximum_speed}, {self.total_km}, {self.max_passengers}, {self.firm}, {self.year_production}")
        
vehicles= Vehicle("OPEL", "ASTRA H", 1.900, 220, 246657, 5)
m_bikes = Motorbike("DUCATI", "DESERTX", 0.937, 263, 55.214, 14.252, True)
cars = Car("MITSUBISHI", "LANCER EVO 9", 2.000, 1200.00, 24.214, "Race", "Gasoline")
buses_1 = Bus("RENAULT", "TRACER", 9.800, 296, 335.147, 30, "Marti-Dani Trans", 2001)
buses_2 = Bus("SCANIA", "TOURING HIGHER", 8.600, 395, 78.270, 49, "Marti-Dani Trans", 2017)
buses_3 = Bus("SCANIA", "INTERLINK", 8.900, 411, 49.000, 32, "Marti-Dani Trans", 2018)
buses_4 = Bus("MERCEDES", "TOURISMO", 10.700, 456, 25.255, 32, "Marti-Dani Trans", 2019)

list_buses=[]
list_buses.append(buses_1)
list_buses.append(buses_2)
list_buses.append(buses_3)
list_buses.append(buses_4)

vehicles.print_info()
m_bikes.print_info()
cars.print_info()
buses_1.print_info()
buses_2.print_info()
buses_3.print_info()
buses_4.print_info()
print(list_buses)
