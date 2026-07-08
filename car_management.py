class Car:
    all_cars = []
    total_cars = 0
    next_car_id = 1
    def __init__(self, make:str, model:str, year:int, milage:int=0, services:list=[]):
        self._id = self.next_car_id
        self._make = make
        self._model = model
        self._year = year
        self._milage = milage
        self._services = services
        Car.all_cars.append(self)
        Car.total_cars += 1
        Car.next_car_id += 1
    @property
    def get_id(self):
        return self._id
    @property
    def details(self):
        return f"ID = {self._id}\nMAKE = {self._make}\nMODEL = {self._model}\nYEAR = {self._year}\nMILAGE = {self._milage}\nSERVICES = {self._services}\n"

    def get_services(self):
        return f"SERVICES: {self._services}"

    def add_service(self, *services:str):
        self._services.extend(services)

    def __str__(self):
        return f"CAR ID {self._id}: {self._year} {self._make} {self._model}"
    def __repr__(self):
        return f"CAR ID {self._id}: {self._year} {self._make} {self._model}"
first_car = Car("Toyota", "Rav4", 2000, 140000)
print(first_car.details)
second_car = Car("Chevrolet", "Malibu", 2013, 40000)
print(second_car.details)
print("adding service record to car 1 and printing details\n")

first_car.add_service("scratch in rear", "headlight replaced", "tires replaced", "totalled")
first_car.add_service("Recovered and rebuilt")

print(first_car.get_services())
