import sys
from random import randint


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
        self.work_matrix = []
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
        out.append([cell.x, cell.y])
        out.append([cell.x + 1, cell.y])

        out.append([cell.x - 1, cell.y + 1])
        out.append([cell.x, cell.y + 1])
        out.append([cell.x + 1, cell.y + 1])

        return [self.cells[e[0]][e[1]] for e in out if self.size > e[0] >= 0 and
                self.size > e[1] >= 0 and e not in no_coords]
    
    def can_place2(self, ship: Ship):
        for i in ship.body:
            for j in self.get_round_cells(i):
                if j.p == '#' or j in self.work_matrix:
                    return False
        return True
    
    def add_ship(self, ship: Ship):
        tt = []
        for i in ship.body:
            try:
                self.cells[i.y][i.x] = i
                k = self.get_round_cells(self.cells[i.y][i.x])
                tt.extend(k)
            except IndexError:
                self.clean_ships()
                return -1
        self.work_matrix.extend(list(set(tt)))
    
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
        self.work_matrix = []
        for i in range(self.size):
            self.cells.append([])
            for j in range(self.size):
                self.cells[i].append(Cell(j, i))

    def gen_ships(self):
        self.clean_ships()
        count_1 = 2
        count_2 = 1
        count_3 = 0
        count_4 = 0
        if self.size == 7:
            count_1 = 2
            count_2 = 1
            count_3 = 1
            count_4 = 0
        elif self.size == 10:
            count_1 = 4
            count_2 = 3
            count_3 = 2
            count_4 = 1
        n = 0
        counts = [count_1, count_2, count_3, count_4]
        counts_cp = counts.copy()
        i = len(counts) - 1
        while i != -1:
            i -= 1
            while counts[i] != 0:
                x, y = self.get_random_coords()
                s = Ship(x, y, i + 1, randint(0, 1) == 1)
                while self.can_place2(s) is False and n < 1000:
                    x, y = self.get_random_coords()
                    s = Ship(x, y, i + 1, randint(0, 1) == 1)
                    n += 1
                if n == 1000:
                    return -1
                counts[i] -= 1
                if self.add_ship(s) == - 1:
                    i = len(counts_cp) - 1
                    counts = counts_cp.copy()
