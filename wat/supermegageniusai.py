from wat.rep import Field, Cell, Ship
from random import randint
import time


class SeaWolf:
    def __init__(self, mapp: Field = None):
        self.next_dots: list[Cell] = []
        self.mapp = mapp
        self.ships = []
        if self.mapp:
            for i in self.mapp.cells:
                for j in i:
                    if j.p == '#':
                        self.ships.append(j)
    
    def shoot(self):
        if not self.next_dots:
            self.next_dots.append(self.gen_random_cell())
        status = self.next_dots[-1].hit()
        while status == -1:
            self.next_dots.pop()
            if len(self.next_dots) == 0:
                self.next_dots.append(self.gen_random_cell())
            status = self.next_dots[-1].hit()
            if status == 1:
                self.add_to_queue(self.next_dots[-1])
        return status

    def set_field(self, field):
        self.mapp = field
        for i in self.mapp.cells:
            for j in i:
                if j.p == '#':
                    self.ships.append(j)
    
    def add_to_queue(self, cell: Cell):
        if cell.x == 0:
            if cell.y == 0:
                self.next_dots.append(self.mapp.cells[0][1])
                self.next_dots.append(self.mapp.cells[1][0])
            elif cell.y == len(self.mapp.cells) - 1:
                self.next_dots.append(self.mapp.cells[cell.y-1][0])
                self.next_dots.append(self.mapp.cells[cell.y][1])
            else:
                self.next_dots.append(self.mapp.cells[cell.y - 1][0])
                self.next_dots.append(self.mapp.cells[cell.y + 1][0])
                self.next_dots.append(self.mapp.cells[cell.y][1])
        elif cell.y == 0:
            if cell.x == 0:
                self.next_dots.append(self.mapp.cells[0][1])
                self.next_dots.append(self.mapp.cells[1][0])
            elif cell.x == len(self.mapp.cells[cell.y]) - 1:
                self.next_dots.append(self.mapp.cells[cell.y][cell.x-1])
                self.next_dots.append(self.mapp.cells[cell.y + 1][cell.x])
            else:
                self.next_dots.append(self.mapp.cells[0][cell.x + 1])
                self.next_dots.append(self.mapp.cells[0][cell.x - 1])
                self.next_dots.append(self.mapp.cells[1][cell.x])
        elif cell.x == len(self.mapp.cells[cell.y]) - 1:
            if cell.y == len(self.mapp.cells) - 1:
                self.next_dots.append(self.mapp.cells[cell.y][cell.x - 1])
                self.next_dots.append(self.mapp.cells[cell.y - 1][cell.x])
            elif cell.y == 0:
                self.next_dots.append(self.mapp.cells[cell.y][cell.x-1])
                self.next_dots.append(self.mapp.cells[cell.y + 1][cell.x])
            else:
                self.next_dots.append(self.mapp.cells[cell.y + 1][cell.x])
                self.next_dots.append(self.mapp.cells[cell.y - 1][cell.x])
                self.next_dots.append(self.mapp.cells[cell.y][cell.x - 1])
        elif cell.y == len(self.mapp.cells) - 1:
            if cell.x == len(self.mapp.cells[cell.y]) - 1:
                self.next_dots.append(self.mapp.cells[cell.y][cell.x - 1])
                self.next_dots.append(self.mapp.cells[cell.y - 1][cell.x])
            elif cell.x == 0:
                self.next_dots.append(self.mapp.cells[cell.y-1][0])
                self.next_dots.append(self.mapp.cells[cell.y][1])
            else:
                self.next_dots.append(self.mapp.cells[cell.y - 1][cell.x])
                self.next_dots.append(self.mapp.cells[cell.y][cell.x + 1])
                self.next_dots.append(self.mapp.cells[cell.y][cell.x - 1])
        else:
            self.next_dots.append(self.mapp.cells[cell.y][cell.x - 1])
            self.next_dots.append(self.mapp.cells[cell.y][cell.x + 1])
            self.next_dots.append(self.mapp.cells[cell.y + 1][cell.x])
            self.next_dots.append(self.mapp.cells[cell.y - 1][cell.x])
            
                
    
    def gen_random_cell(self):
        y = randint(0, len(self.mapp.cells) - 1)
        x = randint(0, len(self.mapp.cells[y]) - 1)
        n = 0
        while not self.mapp.cells[y][x].is_shoted_sparrow() or n <= len(self.mapp.cells) * len(self.mapp.cells[y]):
            y = randint(0, len(self.mapp.cells) - 1)
            x = randint(0, len(self.mapp.cells[y]) - 1)
            n += 1
        return self.mapp.cells[y][x]


class Dummy(SeaWolf):
    def shoot(self):
        status = self.gen_random_cell().hit()
        while status == -1:
            dot = self.gen_random_cell()
            status = dot.hit()
        return status


class ImposibleBot(SeaWolf):
    def shoot(self):
        status = self.ships[-1].hit()
        self.ships.pop()
        return status