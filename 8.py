from abc import ABC, abstractmethod
 
class ChessPiece(ABC):
    def draw(self):
        print("Drew a chess piece")
 
    @abstractmethod
    def move(self):
        pass