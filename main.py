from src.map import Map
from src.ship import ThreeDeckShip


m = Map()
m.generate_map((4, 4))
ship = ThreeDeckShip((0, 0), vertical=False)
print(ship.body)
m.add_ship(ship)
print(m)