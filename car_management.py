class Car:
    all_cars = []
    total_cars = 0
    next_id = 1

    def __init__(self, make:str, model:str, year:int, milage:int=0):
        self._id = Car.next_id
        self._make = make
        self._model = model
        self._year = year
        self.milage = milage
        self._services = []
        Car.next_id += 1
        Car.all_cars.append(self)
    
    @property
    def id(self):
        return self._id
    @property
    def make(self):
        return self._make
    @property
    def model(self):
        return self._model
    @property
    def year(self):
        return self._year
    @property
    def milage(self):
        return self._milage
    @property
    def services(self):
        return self._services
    @make.setter
    def make(self, val):
        if val.isalpha() or val.isalnum():
            self._make = val
        else : 
            raise Exception("Expected letters and numbers only")
    @model.setter
    def model(self, val):
        if val.isalpha() or val.isalnum():
            self._model = val
        else : 
            raise Exception("Expected letters and numbers only")
    @year.setter
    def year(self, val):
        if val.isdigit():
            self._year = int(val)
        else : 
            raise Exception("Expected numbers only")
    @milage.setter
    def milage(self, val):
        if isinstance(val, int):
            self._milage = val
        elif val.isdigit():
            self._milage = int(val)
        # If user inputs empty value, set to default
        elif val == "":
            self._milage = 0
        else : 
            raise Exception("Expected numbers only")
    # add service to list of existing service entries
    def add_service(self, val):
        if val.isalpha() or val.isalnum():
            self.services.append(val)
            return True
        else:
            raise Exception("Expected letters and numbers only")
        
    @classmethod
    def get_total_cars(cls):
        return len(cls.all_cars)
    @classmethod
    def list_cars(cls):
        return cls.all_cars
    @classmethod
    # use binary search to find desired ID of car
    def find_car(cls, car_id:int):

        leftEdge = 0
        rightEdge = len(cls.all_cars) - 1
        while leftEdge <= rightEdge:
            middleVal = (leftEdge + rightEdge) // 2
            if cls.all_cars[middleVal].id > car_id:
                rightEdge = middleVal - 1
            elif cls.all_cars[middleVal].id < car_id:
                leftEdge = middleVal + 1
            else:
                return cls.all_cars[middleVal]
        return False
    
    @classmethod
    # return all details of car. This uses the "find_car" method
    def get_details(cls, car_id:int):
        target_car = cls.find_car(car_id)
        if not target_car:
            return f"Car of ID: {car_id} does not exist"
        return f"\nID:{target_car.id}\nTYPE: {target_car.make} {target_car.model}\nYEAR: {target_car.year}\nMILAGE: {target_car.milage}\nSERVICES: {target_car.services}\n"
    
    def __repr__(self):
        return f"CAR ID:{self._id} - CAR TYPE: {self._make} {self._model}\n"
    def __string__ (self):
        return f"CAR ID:{self._id} - CAR TYPE: {self._make} {self._model}\n"
    
    @classmethod
    # create car from user input. The type checking for this is buggy
    def make_car(cls):
        vals = {"make":input("\nMake of Car (cannot be blank)\n> "),
                "model":input("\nModel of Car (cannot be blank)\n> "),
                "year":input("\nYear of Car (cannot be blank)\n> "),
                "milage":input("\nMilage of Car (default = 0)\n> " )}
        car = cls(**vals)
    
quit_pressed = False

car1 = Car("Toyota", "Model", 2000)
car2 = Car("Chevy", "Model", 2000)
car3 = Car("Subaru", "Model", 2000)
car4 = Car("Mitsubishi", "Model", 2000)
car5 = Car("Jaguar", "Model", 2000)
car6 = Car("Ford", "Model", 2000)
car7 = Car("Make", "Model", 2000)

# run terminal until users quits
while not quit_pressed:
    selection = input(
"""----  WELCOME  ----
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit\n> """)
    # offer all cases for a button press, including a "catch all" at the end
    match selection:
        case "1":
            Car.make_car()
        case "2":
            print(f"\n{Car.list_cars()}")
        case "3":
            print(Car.get_total_cars())
        case "4":
            print(Car.get_details(int(input("Input car ID: > "))))
        case "5":
            user_val = int(input("Input car ID: > "))
            target_car = Car.find_car(user_val)
            if not target_car:
                print(f"Car of ID: {user_val} does not exist")
                continue
            target_car.add_service(input(f"Describe service completed on {target_car.make} {target_car.model}\n> "))
        case "6":
            user_val = int(input("Input car ID: > "))
            target_car = Car.find_car(user_val)
            if not target_car:
                print(f"Car of ID: {user_val} does not exist")
                continue
            target_car.milage = int(input("Input new car milage > "))
        case "7":
            quit_pressed = True
        case _:
            print("invalid input\n")
    print("Hello, World!")