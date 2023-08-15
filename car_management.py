class CarManager:
    all_cars = {}
    total_cars = 0

    def __init__(self, id, make, model, year):
        self._id = id
        self._make = make
        self._model = model
        self._year = year
        self._mileage = 0
        self._services = []

        CarManager.all_cars[self._id] = self 
        CarManager.total_cars += 1

    @property
    def get_id(self):
        return self._id

    @property
    def get_make(self):
        return self._make
    
    @get_make.setter
    def set_make(self, make):
        self._make = make

    @property
    def get_model(self):
        return self._model
    
    @get_model.setter
    def set_model(self, model):
        self._model = model

    @property
    def get_year(self):
        return self._year
    
    @get_year.setter
    def set_year(self, year):
        self._year = year

    @property
    def get_mileage(self):
        return self._mileage
    
    @get_mileage.setter
    def set_mileage(self, mileage):
        if mileage < 0:
            print("Wrong Input")
        else:
            self._mileage = mileage

    @property
    def get_services(self):
        return self._services
    
    @get_services.setter
    def set_services(self, service):
        self._services.append(service)

    def __str__(self):
        return f"""ID: {self.get_id}
Make: {self.get_make}
Model: {self.get_model}
Year: {self.get_year}
Mileage: {self.get_mileage}
Services: {", ".join(self.get_services)}"""

def run_the_manager():
    choice = input("""----  WELCOME  ----
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit\n""")
    match choice:
        case "1":
            id = max(CarManager.all_cars.keys()) if CarManager.all_cars.keys() else 1
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter manufacturing year: "))
            CarManager(id, make, model, year)
            print("Car added successfully!")
            print(CarManager.all_cars)
            return run_the_manager()
        case "2":
            print("All Cars:")
            for car in CarManager.all_cars.values():
                print(f"{car.get_year} {car.get_make} {car.get_model}")
            return run_the_manager()
        case "3":
            print(f"Total number of cars: {CarManager.total_cars}")
            return run_the_manager()
        case "4":
            id = int(input("What is your cars ID?   "))
            print(CarManager.all_cars.get(id))
            return run_the_manager()
        case "5":
            id = int(input("What is your cars ID?   "))
            car = CarManager.all_cars.get(id)
            service = input("Enter service description: ")
            car.set_services = service
            return run_the_manager()
        case "6":
            id = int(input("What is your cars ID?   "))
            car = CarManager.all_cars.get(id)
            mileage = int(input("Enter new mileage: "))
            car.set_mileage = mileage
            return run_the_manager()
        case "7":
            print("Goodbye")
        case _:
            print("Invalid input")
            return run_the_manager()

run_the_manager()