from туц.rep import Field, Ship
m = Field(5)
s1 = Ship(0, 0, 3, rotation=False)
s2 = Ship(0, 3, 3, rotation=False)
m.set_ship(s1)
m.set_ship(s2)
print(m)