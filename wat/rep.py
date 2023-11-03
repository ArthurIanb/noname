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
            for i in range(self.x, self.x + size):
                self.body.append(Cell(i, self.y))
                self.body[-1].set_ship_part()


class Cell:
    def __init__(self, x, y):
        """
            X - Попадание по короблю
            # - Часть корабля
            * - Промах
            _ - Пустая клетка
        """
        self.p = '_'
        self.x = x
        self.y = y

    def is_shoted_sparrow(self):
        return self.p != '*' or self.p != 'X'

    def set_ship_part(self):
        self.p = '#'
    
    def is_alive(self):
        return self.p == '#'
    
    def hit(self):
        if self.p == '#':
            self.p = 'X'
            return 1
        elif self.p == '_':
            self.p = '*'
            return 0
        return -1
    
    def __str__(self) -> str:
        return self.p
    
    def __repr__(self):
        return str(self)


class Field:
    def __init__(self, size):
        self.cells = []
        print(size)
        for i in range(size):
            self.cells.append([])
            for j in range(size):
                self.cells[i].append(Cell(j, i))

    def show_map(self):
        return str(self)
    
    def show_hidden_map(self):
        out = ''
        for i in self.cells:
            for j in i:
                if j.p == '#':
                    out += '_'
                else:
                    out += j.p
            out += '\n'
        return out
    
    def __str__(self) -> str:
        out = ''
        for i in self.cells:
            for j in i:
                out += str(j) + ' '
            out += '\n'
        return out
    
    def add_ship(self, ship: Ship):
        # TODO: добавить проверку на возможность поставить карабля ship
        for i in ship.body:
            try:
                self.cells[i.y][i.x] = i
            except IndexError:
                print('Err')
                print(str(self))
                sys.exit()
    
    def hit_cell(self, x, y):
        try:
            return self.cells[y][x].hit()
        except IndexError:
            sys.exit()
    
    def check_status(self):
        for i in self.cells:
            for j in i:
                if j.is_alive():
                    return True
        return False
