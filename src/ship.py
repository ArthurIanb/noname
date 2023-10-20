import sys


class Point:
    def __init__(self, coord, part_of_ship=False):
        self.coord = coord
        self.is_part_of_ship = part_of_ship

    def __str__(self):
        return f'Point({self.coord[0]}, {self.coord[1]})'
    
    def __repr__(self):
        return str(self)


class ShipPart(Point):
    def __init__(self, coord: tuple):
        super().__init__(coord, part_of_ship=True)
        self.alive = True
    
    def hit(self):
        self.alive = False
    
    def __str__(self):
        status = 'alive' if self.alive else ' dead'
        return super().__str__() + ' ' + status


class Ship:
    def __init__(self, start: tuple, end: tuple):
        if start[1] != end[1] and start[0] != end[0]:
            sys.exit()  
        self.start = start
        self.end = end
        self.body = []
        stay_point = self.start[0] if self.start[0] == self.end[0] else self.start[1]
        if stay_point == self.start[0]:
            print('1')
            print(self.start, self.end)
            for i in range(self.start[1], self.end[1]):
                self.body.append(ShipPart((stay_point, i)))
        else:
            print('2')
            print(self.start, self.end)
            for i in range(self.start[0], self.end[0]):
                self.body.append(ShipPart((i, stay_point)))
        
    def find_dot_with_coord(self, coord):
        for i in self.body:
            if coord == i.coord:
                return i
        return None

    def hit(self, coord: tuple):
        part = self.find_dot_with_coord(coord)
        if part:
            part.hit()
            return 'got ya'
        return 'miss'
    
    def alive(self):
        return any(self.body)
    
    def is_coord_part_of_self(self, coord: tuple):
        return coord[0] in range(self.start[0], self.end[0] + 1) and coord[1] in range(self.start[1], self.end[1] + 1)


class ManyDeckShip(Ship):
    def __init__(self, position: tuple, size: int, vertical = True):
        if vertical:
            end = position[0], position[1] + size
        else:
            end = position[0] + size, position[1]
        print(position, end)
        super().__init__(position, end)
    
    def __str__(self):
        out = ''
        for i in self.body:
            out += f'{i.coord}\n'
        return out


class OneDeckShip(ManyDeckShip):
    def __init__(self, position, vertical = True):
        super().__init__(position, size=1, vertical=vertical)


class TwoDeckShip(ManyDeckShip):
    def __init__(self, position, vertical = True):
        super().__init__(position, size=2, vertical=vertical)


class ThreeDeckShip(ManyDeckShip):
    def __init__(self, position, vertical = True):
        super().__init__(position, size=3, vertical=vertical)


class FourDeckShip(ManyDeckShip):
    def __init__(self, position, vertical = True):
        super().__init__(position, size=4, vertical=vertical)
