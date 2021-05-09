class Furniture:
    pass
    
    def __init__(self, name):
        self.name = name
    


class Storage(Furniture):
    dimension = ""
    amount_of_shelves = 0

    
    def __init__(self, furniture_type, price):
        self.name = furniture_type        # f'Storage {furniture_type}'
        self.price = price
        # super().__init__(name='name')
        # print(furniture_type)

    
class Closet(Storage):
    pass
    
    def made(self, made_of):
        self.made_of = made_of
        super().__init__(made_of)


class Nightstand(Storage):
    pass

    def drawers(self, number_of_drawers):
        self.number_of_drawers = number_of_drawers



class Support(Furniture):


    def __init__(self, name, weight, condition_is_assembled):
        self.name = name
        self.weight = weight
        self.condition_is_assembled = False

class Table(Support):
    height = 0

class Chair(Support):
    has_armrest = False

class Bed(Support):
    is_double_bed = False 


furn1 = Furniture(name='Cabinet furniture')
print(furn1.name, 'is a parent class')

storage = Storage(furniture_type='Storage', price=7000)
closet = Closet(furniture_type='Closet', price='25000')
nightstand = Nightstand(furniture_type='Nightstand', price=8000)

support = Support(name='Support', weight=30, condition_is_assembled=False)
table = Table(name='Table', weight=10, condition_is_assembled=False)
chair = Chair(name='Chair', weight=3, condition_is_assembled=True)
bed = Bed(name='Bed', weight=45, condition_is_assembled=True)


storage.dimension = '800x600x1500'
storage.amount_of_shelves = 5
table.height = 70
chair.has_armrest = True
bed.is_double_bed = True

print(storage.name, 'has 2 more furnitures:')
print(closet.name)
print(nightstand.name)
print('Storages dimension is:', storage.dimension)
print('Closet has', storage.amount_of_shelves, 'shelves')

print(support.name, 'has 3 more furnitures:')
print(table.name)
print(chair.name)
print(bed.name)
print('Has chair armrest?', chair.has_armrest)
print('Is the bed double?', bed.is_double_bed)