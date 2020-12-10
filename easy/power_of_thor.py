light_x, light_y, thor_x, thor_y = [int(i) for i in input().split()]
constraint_x = lambda x: 0 <= x <= 40, [light_x, thor_x]
constraint_y = lambda x: 0 <= x <= 18, [light_y, thor_y]
if not constraint_x:
    raise ValueError("X values cannot be lower than 0 and bigger than 40")
if not constraint_y:
    raise ValueError("Y values cannot be lower than 0 and bigger than 18")

while 1:
    remaining_turns = int(input())
    direction_x = "W" if thor_x > light_x else "E" if thor_x < light_x else ""
    direction_y = "N" if thor_y > light_y else "S" if thor_y < light_y else ""

    if direction_x == "W":
        thor_x -= 1
    if direction_x == "E":
        thor_x += 1

    if direction_y == "S":
        thor_y += 1
    if direction_y == "N":
        thor_y -= 1

    print(direction_y + direction_x)
