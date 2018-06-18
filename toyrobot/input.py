import logging, re

def command(line:str, robot):
    """Parse a line of input and apply the command to the robot (if it is valid).
    May throw if input is invalid."""
    
    m = re.match('^(\w+)\s*([-\w,]*)$', line.strip())
    if not m:
        raise ValueError("Invalid command " + line)
    
    command, args = m.groups()
    args = args.split(',') if args else []

    if command == "PLACE":
        args[0] = int(args[0])
        args[1] = int(args[1])

    getattr(robot, command.title())(*args)
