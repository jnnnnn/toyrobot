"""We need a way to get stdin commands to an instance of the Robot. This class does that."""

import logging
import sys
from .robot import Robot
from .input import command
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if '-v' in args:
        logging.getLogger().setLevel(logging.INFO)

    robot = Robot()
    
    # fileinput will loop through all the lines in the input specified as file names given in 
    # command-line arguments, or the standard input if no arguments are provided.
    while True:
        line = sys.stdin.readline()
        if not line: 
            break # EOF
        try:
            command(line, robot)
        except Exception as e:
            # spec says to ignore bad input lines
            logging.info(line)
            logging.info(e)

if __name__ == "__main__":
    main()