
class House:
    def __init__(self, square):
        self.square = 60

class Room:
    def __init__(self, x, y, z):
        self.square = 50 * z * (x + y)
        self.rooms = []
    def addRooms(self, quant):
        self.rooms.append(House(quant))
    def floor(self):
        how_many = self.square
        for i in self.rooms:
            how_many -= i.square
        return how_many
 
room1 = Room(6, 3, 2.7) 
print(room1.square) 
room1.addRooms(1) 
room1.addRooms(1)
print(room1.floor()) 