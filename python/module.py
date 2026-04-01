def display(text):
    print(text)

# OOPS

class Car:

    __count = 0 # Class variable

    def __init__(self, model, type, year): # Constructor
        self.model = model # self = this keyword
        self.__type = type # Private variable
        self.year = year
        Car.__count += 1

    def get_model(self):
        print(f"Model: {self.model}")
    
    def get_type(self):
        print(f"Type: {self.__type}")

    @staticmethod # Static method(decorator)
    def get_count():
        return Car.__count


my_car = Car("Tesla", "Sedan", 2022)
my_car.get_model()
my_car.get_type()
print(my_car.__type) # Error
print(my_car._Car__type) # Accessing private variable
print(Car.__count)
print(Car.get_count())



# Inheritance

class ElectricCar(Car):

    def __init__(self, model, type, year, battery_size):
        super().__init__(model,type,year)
        self.battery_size = battery_size
    
    def get_battery_size(self):
        print(f"Battery Size: {self.battery_size}")

    @property # Property decorator
    def battery_size(self):
        return self.__battery_size

    @battery_size.setter # Setter decorator
    def battery_size(self, value):
        self.__battery_size = value


my_electric_car = ElectricCar("Tesla", "Sedan", 2022, 100)
my_electric_car.get_model()
my_electric_car.get_battery_size()
my_electric_car.battery_size = 200
my_electric_car.get_battery_size()