class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_into(self):
        return f"[{self.year}][{self.make}][{self.model}]"

first_car = Car("Toyota", "Corolla", 2020)
print(first_car.get_into())