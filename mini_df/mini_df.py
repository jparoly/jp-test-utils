#!/usr/bin/python3
from argparse import ArgumentParser
import shutil


def setup_parser():
    """Configure command line argument parser object."""

    parser = ArgumentParser(description='outputs disk total, free '
                            'and used space for each entry in PATH',
                            add_help=False)
    # parser.add_argument('-h', '--help', action='help', help='show this help '
    #                     'message and exit')
    parser.add_argument('paths', metavar='PATH', nargs='*', default=None,
                        help='the path in which to list disk stats')
    parser.add_argument('-h', '--prettier', action='store_true',
                        help='make more human readable')
    return parser


def print_pretty(stats):
    print(f'Total Disk Space: {stats[0]}')
    print(f'Used Disk Space: {stats[1]}')
    print(f'Free Disk Space: {stats[2]}\n')


def get_disk_stats(paths, prettier):
    if not paths:
        stats = shutil.disk_usage('/')
        if prettier:
            print('\n*** Disk Usage for the Current Path ***\n')
            print_pretty(stats)
        else:
            print(f'current path {stats}')
    else:
        for path in paths:
            stats = shutil.disk_usage(path)
            if prettier:
                print(f'\n*** Disk Usage for "{path}" ***\n')
                print_pretty(stats)
            else:
                print(f'{path} {stats}')


def main():
    parser = setup_parser()
    args = parser.parse_args()
    paths = args.paths
    prettier = args.prettier
    get_disk_stats(paths, prettier)

    # TODO: Add error handling


if __name__ == '__main__':
    main()
