import sys
from random import randint, choice

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
        self.size = size
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

    def can_place(self, ship):
        last_x, last_y = -1, -1
        for i in ship.body:
            try:
                if self.cells[i.y][i.x].p == '#':
                    return False
            except IndexError:
                return False
        return True
    
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

    def get_random_cell(self):
        y = randint(0, len(self.cells) - 1)
        x = randint(0, len(self.cells[y]) - 1)
        n = 0
        while self.cells[y][x].p == '#':
            y = randint(0, len(self.cells) - 1)
            x = randint(0, len(self.cells[y]) - 1)
            n += 1
            if n == 201:
                return -1
        return x, y

    def clean_ships(self):
        self.cells = []
        for i in range(self.size):
            self.cells.append([])
            for j in range(self.size):
                self.cells[i].append(Cell(j, i))

    def gen_ships(self):
        print('genships')
        sizes = {
            3: 1,
            2: 1,
            1: 0,
        }
        if self.size == 5:
            sizes[3] = 1
            sizes[2] = 2
            sizes[1] = 2
        elif self.size == 7:
            sizes[3] = 1
            sizes[2] = 2
            sizes[1] = 2
        elif self.size == 10:
            sizes[3] = 1
            sizes[2] = 2
            sizes[1] = 2
        stop = 0
        while sizes:
            stop += 1
            if stop == 200:
                sys.exit()
            if 3 in sizes.keys() and sizes[3] == 0:
                del sizes[3]
            if 2 in sizes.keys() and sizes[2] == 0:
                del sizes[2]
            if 1 in sizes.keys() and sizes[1] == 0:
                del sizes[1]
            if not sizes:
                break
            size = choice(list(sizes.keys()))
            ss = self.get_random_cell()
            if ss == -1:
                break
            x, y = ss
            rotation = randint(0, 1)

            s = Ship(x, y, size, rotation == 1)
            if self.can_place(s):
                sizes[size] -= 1
                self.add_ship(s)
        print(stop)

"""
TODO: get around cells: function to avoid placing ships together
"""