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
    
    def get_round_cells(self, cell, no_coords=None):
        out = []
        if not no_coords:
            no_coords = []
        out.append([cell.x - 1, cell.y - 1])
        out.append([cell.x, cell.y - 1])
        out.append([cell.x + 1, cell.y - 1])

        out.append([cell.x - 1, cell.y])

        out.append([cell.x + 1, cell.y])

        out.append([cell.x - 1, cell.y + 1])
        out.append([cell.x, cell.y + 1])
        out.append([cell.x + 1, cell.y + 1])

        return [self.cells[e[0]][e[1]] for e in out if self.size > e[0] >= 0 and self.size > e[1] >= 0 and e not in no_coords]


    def can_place(self, ship):
        last_x, last_y = -1, -1
        for i in ship.body:
            try:
                if self.cells[i.y][i.x].p == '#':
                    return False
                if last_x == -1 and last_y == -1:
                    if self.cells[i.y][i.x].p == '#':
                        return False
                    for j in self.get_round_cells(self.cells[i.y][i.x]):
                        if j.p == '#':
                            return False
                    last_x = i.x
                    last_y = i.y
                else:
                    for j in self.get_round_cells(self.cells[i.y][i.x], no_coords=[[last_x, last_y]]):
                        if j.p == '#':
                            return False

            except IndexError:
                return False
        return True
    
    def add_ship(self, ship: Ship):
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

    def get_random_coords(self):
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
        print(self)
        self.clean_ships()
        nn = 0
        print('genships2')
        count_1 = 2
        count_2 = 1
        count_3 = 1
        count_4 = 0
        if self.size == 7:
            count_1 = 2
            coutn_2 = 1
            count_3 = 1
            count_4 = 0
        elif self.size == 10:
            count_1 = 4
            count_2 = 3
            count_3 = 2
            count_4 = 1
        counts = [count_1, count_2, count_3, count_4]
        for i in range(len(counts)):
            while counts[i] != 0:
                x, y = self.get_random_coords()
                s = Ship(x, y, i + 1, randint(0, 1) == 1)
                if self.can_place(s):
                    self.add_ship(s)
                    counts[i] -= 1
                nn += 1
                if nn == 100:
                    print(f'c_{i+1}:n=100')
                    return -1


    def gen_ships1(self):
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
            sizes[3] = 2
            sizes[2] = 2
            sizes[1] = 3
        elif self.size == 10:
            sizes[4] = 1
            sizes[3] = 2
            sizes[2] = 3
            sizes[1] = 4
        stop = 0
        stop_2 = 0
        while sizes:
            stop += 1
            if stop == 200:
                self.clean_ships()
                stop = 0
                stop_2 += 1
            if stop_2 == 100:
                print('stop_2')
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
            ss = self.get_random_coords()
            if ss == -1:
                break
            x, y = ss
            rotation = randint(0, 1)

            s = Ship(x, y, size, rotation == 1)
            if self.can_place(s):
                sizes[size] -= 1
                self.add_ship(s)
        print(stop)
        print(self)


f = Field(5)
print(f.get_round_cells(f.cells[4][4], no_coords=[[3, 3], [3, 4]]))