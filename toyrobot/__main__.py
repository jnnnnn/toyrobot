import fileinput
import logging
import sys
from .robot import Robot

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
            robot.Command(line)
        except Exception as e:
            logging.info(line)
            logging.info(e)
            pass # ignore dodgy lines

if __name__ == "__main__":
    main()