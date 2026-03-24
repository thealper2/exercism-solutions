# Globals for the directions
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

DIRECTION_MAP = {
    NORTH: "north",
    EAST: "east",
    SOUTH: "south",
    WEST: "west",
}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x = x_pos
        self.y = y_pos

    def move(self, instructions):
        for instruction in instructions:
            if instruction == "R":
                self._turn_right()
            elif instruction == "L":
                self._turn_left()
            elif instruction == "A":
                self._advance()

    def _turn_right(self):
        idx = (DIRECTIONS.index(self.direction) + 1) % 4
        self.direction = DIRECTIONS[idx]

    def _turn_left(self):
        idx = (DIRECTIONS.index(self.direction) - 1) % 4
        self.direction = DIRECTIONS[idx]

    def _advance(self):
        dx, dy = self.direction
        self.x += dx
        self.y += dy

    @property
    def coordinates(self):
        return (self.x, self.y)

    def direction_name(self):
        return DIRECTION_MAP[self.direction]
