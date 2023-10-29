from wat.rep import Field, Ship
from wat.supermegageniusai import Dummy
class Game:
    def main():
        coords = [
            (0, 0, 3, False),
            (4, 0, 4, True),
            (1, 2, 2, False),
            (0, 4, 1, False)
        ]

        coords2 = [
            (0, 1, 3, True),
            (2, 1, 1, False),
            (4, 0, 2, True),
            (2, 3, 2, False)
        ]

        computer_field = Field(5)
        human_field = Field(5)
        sf = Dummy(human_field)
        for i in coords:
            s = Ship(*i)
            computer_field.add_ship(s)

        for i in coords2:
            s = Ship(*i)
            human_field.add_ship(s)

        human_turn = False
        while human_field.check_status() and computer_field.check_status():
            if not human_turn:
                if sf.shoot() == 0:
                    print('comp missed')
                else:
                    print('he is got ya')
            else:
                ok = False
                status = -1
                while status == -1:
                    print('Координаты: ')
                    print('x:', end=' ')
                    x = int(input())
                    print('y: ', end='')
                    y = int(input())
                    status = computer_field.hit_cell(x, y)
                if status == 0:
                    print('miss')
                else:
                    print('In apple')
            input()
            human_turn = not human_turn

            print('Computer field')
            print(computer_field)
            print('Youre field')
            print(human_field)