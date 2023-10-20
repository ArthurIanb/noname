from туц.rep import Field, Ship

size = 5
f1 = Field(size)
f2 = Field(size)

ship1 = Ship(0, 0, 3)
ship2 = Ship(0, 0, 3, rotation=False)
f1.set_ship(ship1)
f2.set_ship(ship2)

while f1.check_status() and f2.check_status():
    print(f2.show_hidden_map())
    print('f1')
    x, y = map(int, input().split())
    if f2.hit_cell(x, y):
        print("You got it")
    print(f1.show_hidden_map())
    print('f2 shoots')
    x, y = map(int, input().split())
    if f1.hit_cell(x, y):
        print('f2, you got it')

if f1.check_status():
    print('f1 you are winner')
else:
    print('f2 you are winner')
