import unittest
import random
from toyrobot.robot import Robot, DIR

class RobotTestCase(unittest.TestCase):
    """Tests for `robot.py`."""

    def setUp(self):
        self.robot = Robot()

    def test_simple(self):
        """Test basic commands for the robot"""
        self.robot.Place(0,0,'NORTH')
        # whitespace in commands should be OK
        self.robot.Move()
        self.assertEqual(self.robot.x, 0)
        self.assertEqual(self.robot.y, 1)
        self.robot.Left()
        self.assertEqual(self.robot.f, DIR['WEST'])
        self.robot.Place(2,2,'EAST')
        self.robot.Right()
        self.assertEqual((self.robot.x,self.robot.y,self.robot.f), (2,2,DIR['SOUTH']))
        
    def test_turns(self):
        """Ensure that turning works properly."""
        directions = ['NORTH','EAST','SOUTH','WEST']
        self.robot.Place(0,0,'WEST')
        for direction in directions:
            self.robot.Right()
            self.assertEqual(self.robot.f, DIR[direction])

        for direction in directions[::-1]:
            self.assertEqual(self.robot.f, DIR[direction])
            self.robot.Left()

    def test_bounds(self):
        """The robot must stay on the table (x,y in [0..4])."""
        edge_states = [
            (0,0,"WEST"),
            (0,4,"NORTH"),
            (4,0,"SOUTH"),
            (4,4,"EAST")]
        for x,y,f in edge_states:
            with self.subTest(edge_state=(x,y,f)):
                self.robot.Place(x,y,f)
                with self.assertRaises(Exception):
                    self.robot.Move() # off the edge
        
    def test_edge_cases(self):
        """Make sure we can't place the robot in an even slightly invalid position"""
        for x in [-1,0,4,5]:
            for y in [-1,0,4,5]:
                with self.subTest(x=x,y=y):
                    command = "PLACE {x},{y},NORTH".format(**locals())
                    if 0<=x<=4 and 0<=y<=4:
                        self.robot.Place(x,y,"NORTH")
                        self.assertEqual((self.robot.x,self.robot.y,self.robot.f), (x,y,DIR['NORTH']))
                    else:
                        with self.assertRaises(Exception):
                            self.robot.Place(x,y,"NORTH")

    def disabled_test_malformed_commands(self):
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
        self.robot.Place(0,0,'NORTH')
        for i in range(100000):
            self.robot.Move()
            self.robot.Right()