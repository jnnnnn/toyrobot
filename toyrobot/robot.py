"""A class representing the toy robot."""

import collections

# We need to map direction names to the resulting movement translations
# for example, a robot facing north will move 1 unit in the y direction
# In order of turning right
Movement = collections.namedtuple('Movement', ['x', 'y'])
MOVEMENTS = collections.OrderedDict([
    ('NORTH', Movement(x=0, y=1)),
    ('EAST', Movement(x=1, y=0)),
    ('SOUTH', Movement(x=0, y=-1)),
    ('WEST', Movement(x=-1, y= 0)),
])
DIRECTIONS = list(MOVEMENTS.keys())
TURN_RIGHT = { direction: DIRECTIONS[(i+1)%len(DIRECTIONS)] for i, direction in enumerate(DIRECTIONS)}
TURN_LEFT  = { direction: DIRECTIONS[(i-1)%len(DIRECTIONS)] for i, direction in enumerate(DIRECTIONS)}


class Robot:
    """Keeps track of where a toy robot is."""
    def __init__(self):
        self.x = None # x-coordinate on table, 0..4
        self.y = None # y-coordinate on table, 0..4
        self.f = None # direction robot is facing

    def _set(self, x, y, f):
        if x >= 5 or x < 0:
            raise ValueError('x out of bounds')
        elif y >= 5 or y < 0:
            raise ValueError('y out of bounds')
        elif f not in MOVEMENTS:
            raise ValueError('unknown direction')
        self.x = x
        self.y = y
        self.f = f

    def Command(self, command:str):
        """Execute a command such as MOVE or REPORT."""
        command = command.strip()
        if command.startswith('PLACE'):
            x, y, f = command.split('PLACE')[1].split(',')
            x, y = int(x), int(y)
            f = f.strip()
            # parsing complete, update state
            self._set(x, y, f)
        # The remaining commands require that we are initialized
        elif self.f:
            if command == 'MOVE':
                direction = MOVEMENTS[self.f]
                self._set(
                    x = self.x + direction.x,
                    y = self.y + direction.y,
                    f = self.f
                )
            elif command == 'LEFT':
                self.f = TURN_LEFT[self.f]
            elif command == 'RIGHT':
                self.f = TURN_RIGHT[self.f]
            elif command == 'REPORT':
                print("{x},{y}: {f}".format(**self.__dict__))
            else:
                raise ValueError("Invalid command %s" % command)
        else:
            raise ValueError("Uninitialized.")
        