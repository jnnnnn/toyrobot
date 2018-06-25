"""Complete system tests, including input and parsing."""

import unittest
import io
import sys
import textwrap
import collections
from toyrobot.__main__ import main

class RobotCommandTests(unittest.TestCase):
    """Tests for the complete system: input parsing, commands movement, and output."""

    def _test(self, input, expected_output):
        input = io.StringIO(textwrap.dedent(input))
        output = io.StringIO()
        sys.stdin = input
        sys.stdout = output
        main()
        self.assertEqual(output.getvalue(), expected_output)

    def test_simple(self):
        self._test(input="""
            MOVE
            PLACE 2,2,NORTH
            REPORT
            MOVE
            MOVE
            MOVE 2
            REPORT
            """, 
            expected_output="""2,2: NORTH\n2,4: NORTH\n""")

    def test_malformed(self):
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
        for invalid_command in invalid_commands:
            input = """PLACE 3,2,EAST
                       {invalid_command}
                       REPORT
                       """.format(invalid_command=invalid_command)
            with self.subTest(input=input):
                expected_output = "3,2: EAST\n"
                self._test(input, expected_output)

    
    def test_uninitialized(self):
        commands = [
            "MOVE",
            "LEFT",
            "RIGHT",
            "REPORT",
        ]
        for command in commands:
            input = """{command}
                       REPORT
                       PLACE 2,3,SOUTH
                       MOVE
                       REPORT
                       """.format(command=command)
            with self.subTest(input=input):
                expected_output = "2,2: SOUTH\n"
                self._test(input, expected_output)


        