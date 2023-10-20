import sys
class Ship:
    def __init__(self, x, y, size, rotation=True) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.health = size
        self.rotation = rotation
        self.body = []
        if rotation:
            for i in range(self.y, self.y + size):
                self.body.append(Cell(self.x, i))
                self.body[-1].set_ship_part()
        else:
            for i in range(self.x, self.y + size):
                self.body.append(Cell(i, self.y))
                self.body[-1].set_ship_part()


class Cell:
    def __init__(self, x, y):
        self.p = '_'
        self.x = x
        self.y = y

    def set_ship_part(self):
        self.p = '#'
    
    def set_ship_destr(self):
        self.p = 'X'
    
    def set_miss(self):
        self.p = '*'
    
    def is_alive(self):
        return self.p == '#'
    
    def hit(self):
        if self.p == '#':
            self.set_ship_destr()
        else:
            self.set_miss()
    
    def __str__(self) -> str:
        return self.p


class Field:
    def __init__(self, size):
        self.cells = []
        for i in range(size):
            self.cells.append([])
            for j in range(size):
                self.cells[i].append(Cell(j, i))
    
    def __str__(self) -> str:
        out = ''
        for i in self.cells:
            for j in i:
                out += str(j)
            out += '\n'
        return out
    
    def set_ship(self, ship: Ship):
        for i in ship.body:
            try:
                self.cells[i.y][i.x] = i
            except IndexError:
                sys.exit()
    
    def hit_cell(self, x, y):
        try:
            self.cells[y][x].hit()
        except IndexError:
            sys.exit()
    
    def check_status(self):
        for i in self.cells:
            for j in i:
                if j.is_alive():
                    return True
        return False


f = Field(4)
ship = Ship(1, 1, 3, rotation=False)
f.set_ship(ship)
while f.check_status():
    f.hit_cell(*tuple(map(int, input().split())))
    print(f)