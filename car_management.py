


class Car:
    all_cars = {}
    total_cars = 0
    car_id = 0

    def __init__(self, make, model, year, mileage):
        self._id = self.generate_id()
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._service = None
        self.all_cars[self.car_id] = self

    @classmethod
    def generate_id(cls):
        cls.car_id += 1
        cls.total_cars += 1
        return cls.car_id

    @classmethod
    def add_car(cls):
        make = input("make\n")
        model = input("model\n")
        year = input("year\n")
        mileage = input("mileage\n")
        Car(make, model, year, mileage)

    @classmethod
    def view_all_cars(cls):
        print(cls.all_cars)

    @classmethod
    def view_total_cars(cls):
        print(cls.total_cars)

    @classmethod
    def view_car_details(cls, id):
        return cls.all_cars[id]        
    
    def add_services(service, serviced_car):
        if serviced_car._service == None:
            serviced_car._service = []
        serviced_car._service.append(service)

    def update_mileage(new_miles, car):
        if new_miles < 0:
            raise Exception("Must be greater than 0!")
        car._mileage = new_miles
    

    def __repr__(self):
        service_str = "None"
        if (self._service != None):
            service_str = ", ".join(self._service)
        return f"{self._make} - {self._model} - {self._year} - {self._mileage} - {service_str}"


def main():
    while True:
        print("""
        ----  WELCOME  ----
    1. Add a car
    2. View all cars
    3. View total number of cars
    4. See a car's details
    5. Service a car
    6. Update mileage
    7. Quit
    Select an option from the menu:\n""")
        user_input = int(input("Select an option from the menu:\n"))
        if (user_input == 7):
            break
        elif (user_input == 1):
            Car.add_car()
        elif (user_input == 2):
            Car.view_all_cars()
        elif (user_input == 3):
            Car.view_total_cars()
        elif (user_input == 4):
            cars_id = int(input("Car ID:\n"))
            print(Car.view_car_details(cars_id))
        elif (user_input == 5):
            this_cars_id = int(input("Car ID:\n"))
            serviced_car = Car.all_cars[this_cars_id]
            service_str = input("Service performed:")
            Car.add_services(service_str, serviced_car)
        elif (user_input == 6):
            this_cars_id = int(input("Car ID:\n"))
            car = Car.all_cars[this_cars_id]
            new_mileage = int(input("New Mileage:"))
            Car.update_mileage(new_mileage, car)



main()



