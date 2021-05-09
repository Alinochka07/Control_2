class Car:
    maker = "Toyota"

    def __init__(self, name, maker):
        self.name = name
        self.maker = maker

    def info(self):
        print(f'This car is {self.name}. The maker is {self.maker}')

    def volume(self):
        print(2)

class Toyota_sedan(Car):
    pass

yaris = Car('Yaris', 'Toyota')
print(yaris)
print(yaris.name)
yaris.info()