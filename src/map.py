from src.ship import *

class Map:
    def __init__(self):
        self.field = []
    
    def generate_map(self, size):
        w, h = size
        for i in range(h):
            self.field.append([])
            for j in range(w):
                self.field[i].append(Point((j, i)))
    def add_ship(self, ship: Ship):
        for i in ship.body:
            self.field[i.coord[0]][i.coord[1]] = ShipPart(i.coord)
        
    def __str__(self):
        out = ''
        n = 1
        for i in self.field:
            for j in i:
                if j.is_part_of_ship:
                    out += '#'
                else:
                    out += '_'
            out += '\n'
        return out
