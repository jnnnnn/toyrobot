"""A class representing the toy robot."""

import collections
Movement = collections.namedtuple('Movement', ['x', 'y', 'right', 'left'])
Directions = {
    'NORTH': Movement(x= 0, y= 1, right='EAST' , left='WEST' ),
    'EAST' : Movement(x= 1, y= 0, right='SOUTH', left='NORTH'),
    'SOUTH': Movement(x= 0, y=-1, right='WEST' , left='EAST' ),
    'WEST' : Movement(x=-1, y= 0, right='NORTH', left='SOUTH'),
}

class Robot:
    """Keeps track of where a toy robot is."""
    def __init__(self):
        self.x = None
        self.y = None
        self.f = None

    def _set(self, x, y, f):
        if x >= 5 or x < 0:
            raise ValueError('x out of bounds')
        elif y >= 5 or y < 0:
            raise ValueError('y out of bounds')
        elif f not in Directions:
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
            # parsing complete, update state
            self._set(x, y, f)
            return

        # The remaining commands require that we are initialized
        if not self.f:
            return

        if command == 'MOVE':
            direction = Directions[self.f]
            self._set(
                x = self.x + direction.x,
                y = self.y + direction.y,
                f = self.f
            )
        elif command == 'LEFT':
            direction = Directions[self.f]
            self.f = direction.left
        elif command == 'RIGHT':
            direction = Directions[self.f]
            self.f = direction.right
        elif command == 'REPORT':
            print("{x},{y}: {f}".format(self))
            