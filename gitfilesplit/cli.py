#!/usr/bin/env python3
import argparse
import logging

from gitfilesplit import VERSION_STR
from gitfilesplit.toolbox import split, configure_logging


def main():

    arg_parser = argparse.ArgumentParser(
        prog='gitfilesplit',
        description='Command line helper to Git split one file into several preserving history'
    )
    arg_parser.add_argument('--version', action='version', version=VERSION_STR)
    arg_parser.add_argument('source', help='Source filename to split')
    arg_parser.add_argument('targets', nargs='*', help='One or more target filenames to split source into')

    args = arg_parser.parse_args()

    split(source=args.source, targets=args.targets)


if __name__ == '__main__':
    configure_logging(logging.INFO)
    main()
