import unittest
import random
from toyrobot.robot import Robot

class RobotTestCase(unittest.TestCase):
    """Tests for `robot.py`."""

    def setUp(self):
        self.robot = Robot()

    def test_simple(self):
        """Test basic commands for the robot"""
        self.robot.Command("PLACE 0, 0, NORTH")
        # whitespace in commands should be OK
        self.robot.Command(" MOVE ")
        self.assertEqual(self.robot.x, 0)
        self.assertEqual(self.robot.y, 1)
        self.robot.Command("LEFT")
        self.assertEqual(self.robot.f, 'WEST')
        self.robot.Command("PLACE 2,2,EAST")
        self.robot.Command("RIGHT")
        self.assertEqual((self.robot.x,self.robot.y,self.robot.f), (2,2,'SOUTH'))
        
    def test_turns(self):
        """Ensure that turning works properly."""
        directions = ['NORTH','EAST','SOUTH','WEST']
        self.robot.Command("PLACE 0,0,WEST")
        for direction in directions:
            self.robot.Command("RIGHT")
            self.assertEqual(self.robot.f, direction)

        for direction in directions[::-1]:
            self.assertEqual(self.robot.f, direction)
            self.robot.Command("LEFT")

    def test_bounds(self):
        """The robot must stay on the table (x,y in [0..4])."""
        edge_states = [
            (0,0,"WEST"),
            (0,4,"NORTH"),
            (4,0,"SOUTH"),
            (4,4,"EAST")]
        for x,y,f in edge_states:
            with self.subTest(edge_state=(x,y,f)):
                self.robot.Command("PLACE {x},{y},{f}".format(**locals()))
                with self.assertRaises(Exception):
                    self.robot.Command("MOVE") # off the north edge
        
    def test_edge_cases(self):
        """Make sure we can't place the robot in an even slightly invalid position"""
        for x in [-1,0,4,5]:
            for y in [-1,0,4,5]:
                with self.subTest(x=x,y=y):
                    command = "PLACE {x},{y},NORTH".format(**locals())
                    if 0<=x<=4 and 0<=y<=4:
                        self.robot.Command(command)
                        self.assertEqual((self.robot.x,self.robot.y,self.robot.f), (x,y,"NORTH"))
                    else:
                        with self.assertRaises(Exception):
                            self.robot.Command(command)

    def test_malformed_commands(self):
        """Malformed commands must be ignored, and must not affect the robot's state."""
        invalid_commands = [
            "PLAC 0,0,NORTH",
            "PLACE 0,NORTH",
            "PLACE 0,0,0,NORTH",
            "PLACE 0,0,NORT",
            "PLACE 0,EAST,EAST",
            "PLACE 0,0,0",
            "PLACE",
            "",
            " ",
            "X",
            "MOVE 1",
            "TURN RIGHT",
            "RIGH",
            "LEFTT",
            "REPORT TWICE",
        ]
        self.robot.Command("PLACE 3,2,EAST")
        for command in invalid_commands:
            with self.subTest(command=command):
                with self.assertRaises(Exception):
                    self.robot.Command(command)
                self.assertEqual((self.robot.x,self.robot.y,self.robot.f), (3,2,'EAST'))

    def test_long(self):
        """Feed many commands into the robot to make sure it behaves itself."""
        self.robot.Command("PLACE 0,0,NORTH")
        for i in range(100000):
            self.robot.Command("MOVE")
            self.robot.Command("RIGHT")