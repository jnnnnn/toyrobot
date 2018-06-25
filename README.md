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

`F` is a direction, one of

            NORTH
        WEST     EAST
            SOUTH

The southwest corner of the tabletop is at `X,Y = 0,0`.

The robot is constrained to move within the table (`X,Y ∈ [0..4]`)

## Setup

Install Python 3.6+, clone this repository, and run this in the root folder:

    pip install -e .

## Development

To run tests, use:

    pip install pytest
    pytest

For `stderr` logging of the problems with invalid commands, run with the `-v` switch.

For a code coverage report, use:

    pip install pytest-cov
    pytest --cov=toyrobot --cov-report html:cov_html

## Bibliography

1. https://stackoverflow.com/questions/4740473/setup-py-examples
2. https://docs.python.org/3/distutils/setupscript.html
3. https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
4. https://docs.pytest.org/en/latest/goodpractices.html