"""Console application to read two file paths."""

import argparse
import sys

from subimage import epilog
from subimage.core import run_all


def parse_args(args):
    """Parse provided runtime arguments.

    Args:
        args (list): all parseable input arguments

    Returns:
        dict: all parsed arguments

    """
    # https://docs.python.org/3/howto/argparse.html
    parser = argparse.ArgumentParser(description=__doc__, epilog=epilog)
    parser.add_argument(
        "images",
        metavar="IMAGE",
        type=str,
        nargs="+",
        help="path to an input image to cross correlate",
    )
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Enable verbose logging"
    )
    return parser.parse_args(args)


def main():
    """Read CLI args and convert into named arguments.

    Returns:
        tuple: top-left x,y position of a successful match

    """
    # TODO: should override any config from system/local/env
    return run_all(**vars(parse_args(sys.argv[1:])))
