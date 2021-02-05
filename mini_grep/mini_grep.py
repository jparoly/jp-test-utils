#!/usr/bin/python3
import os
import re
import sys
from argparse import ArgumentParser


def grep_file(pattern: str, file, print_lineno: bool):
    """Search files or standard input."""
    text = sys.stdin if file == '(standard input)' else open(file, 'r')

    line = text.readline()
    lineno = 1

    while line:
        if re.search(pattern, line):
            if not print_lineno:
                print(line.rstrip())
            else:
                print(f'{lineno} {line}'.rstrip())
        line = text.readline()
        lineno += 1
    text.close()


def grep_files(pattern: str, files, print_lineno: bool):
    """Search files and directories."""

    for file in files:
        if os.path.isfile(file) or file == '(standard input)':
            grep_file(pattern, file, print_lineno)


def setup_parser():
    """Configure command line argument parser object."""

    parser = ArgumentParser(description='Finds and prints lines of file(s) '
                            'that match provided pattern. Prints line '
                            'number as well if -q is not provided.',
                            add_help=False)
    parser.add_argument('-h', '--help', action='help', help='show this help '
                        'message and exit')
    parser.add_argument('-e', '--pattern', type=str, required=True,
                        help='the pattern to find')
    parser.add_argument('files', metavar='FILES', nargs='*', default=['-'],
                        help='the files(s) to search')
    parser.add_argument('-q', '--no-line-number', action='store_true',
                        help='do not print line numbers')
    return parser


def main():
    parser = setup_parser()
    args = parser.parse_args()
    pattern = args.pattern

    try:
        re.compile(pattern)
    except re.error:
        sys.exit('Please make sure the pattern is valid regex.')

    files = [f if f != '-' else '(standard input)' for f in args.files]

    print_lineno = True
    if args.no_line_number:
        print_lineno = False

    grep_files(pattern, files, print_lineno)


if __name__ == '__main__':
    main()
