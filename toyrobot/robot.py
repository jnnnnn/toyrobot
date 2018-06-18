"""A class representing the toy robot."""

import collections
from enum import Enum

DIR = Enum("Direction", "NORTH EAST SOUTH WEST")

# We need to map direction names to the resulting movement translations
# for example, a robot facing north will move 1 unit in the y direction
# In order of turning right
Movement = collections.namedtuple('Movement', ['x', 'y', 'left', 'right'])
MOVEMENTS = {
    DIR.NORTH: Movement(x=0, y=1, left=DIR.WEST, right=DIR.EAST),
    DIR.EAST: Movement(x=1, y=0, left=DIR.NORTH, right=DIR.SOUTH),
    DIR.SOUTH: Movement(x=0, y=-1, left=DIR.EAST, right=DIR.WEST),
    DIR.WEST: Movement(x=-1, y= 0, left=DIR.SOUTH, right=DIR.NORTH),
}

TABLE_COORD_MIN = 0
TABLE_COORD_MAX = 4

class Robot:
    """Keeps track of where a toy robot is."""
    def __init__(self):
        self.x = None # x-coordinate on table, 0..4
        self.y = None # y-coordinate on table, 0..4
        self.f = None # direction robot is facing

    def Place(self, x:int, y:int, f:str):
        if x < TABLE_COORD_MIN or x > TABLE_COORD_MAX:
            raise ValueError('x out of bounds')
        elif y < TABLE_COORD_MIN or y > TABLE_COORD_MAX:
            raise ValueError('y out of bounds')
        elif f not in DIR.__members__:
            raise ValueError('%s is not a valid direction' % f)
        self.x = x
        self.y = y
        self.f = DIR[f]

    def Move(self):
        movement = MOVEMENTS[self.f]
        self.Place(
            x = self.x + movement.x,
            y = self.y + movement.y,
            f = self.f.name)

    def Left(self):
        self.f = MOVEMENTS[self.f].left

    def Right(self):
        self.f = MOVEMENTS[self.f].right

    def Report(self):
        print("{x},{y}: {f.name}".format(**self.__dict__))