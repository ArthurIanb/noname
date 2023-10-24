from туц.rep import Field, Cell, Ship


class SeaWolf:
    def __init__(self, mapp: Field = None):
        self.next_dots: list[Cell] = []
        self.mapp = mapp
    
    def shoot(self):
        if self.next_dots:
            cell = self.next_dots[0]
            self.next_dots = self.next_dots[1:]
        else:
            self.next_dots.append(self.gen_random_cell())
            return self.shoot()
        if cell.is_shoted_sparrow():
            return self.shoot()
        
        if cell.hit() == 1:
            self.add_to_queue(cell)
        else:
            self.next_dots.append(self.gen_random_cell())
            self.shoot()
    
    def add_to_queue(self, cell: Cell):
        if cell.x == 0:
            if cell.y == 0:
                self.next_dots.append(self.mapp[0][1])
                self.next_dots.append(self.mapp[1][0])
            else:
                self.next_dots.append(self.mapp[cell.y - 1][0])
                self.next_dots.append(self.mapp[cell.y + 1][0])
                self.next_dots.append(self.mapp[cell.y][1])
        elif cell.y == 0:
            if cell.x == 0:
                self.next_dots.append(self.mapp[0][1])
                self.next_dots.append(self.mapp[1][0])
            else:
                self.next_dots.append(self.mapp[0][cell.x + 1])
                self.next_dots.append(self.mapp[0][cell.x - 1])
                self.next_dots.append(self.mapp[1][cell.x])
        
                
            
                
    
    def gen_random_cell(self):
        ...


