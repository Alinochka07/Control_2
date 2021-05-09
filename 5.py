
    

class Car:
    maker = "Toyota"

    def __init__(self, name, maker):
        self.name = name
        self.maker = maker



class Toyota_sedan(Car):
    pass

yaris = Car(name='Yaris', maker='Toyota')
print(yaris)
print(yaris.name)