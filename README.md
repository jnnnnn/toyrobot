# Toy Robot

The application is a simulation of a toy robot moving on a square table top.

## Usage

After setup, run the command line program with the command

    toyrobot

The following commands are permitted:

    PLACE X,Y,F
    MOVE
    LEFT
    RIGHT
    REPORT

The robot is constrained to move within the table (`X,Y ∈ [0..4]`)

## Setup

    pip install -e .

## Development

To run tests, use:

    pytest

For `stderr` logging of the problems with invalid commands, run with the `-v` switch.

## Bibliography

1. https://stackoverflow.com/questions/4740473/setup-py-examples
2. https://docs.python.org/3/distutils/setupscript.html
3. https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
4. https://docs.pytest.org/en/latest/goodpractices.html