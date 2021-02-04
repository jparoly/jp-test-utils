#!/usr/bin/python3
import os
from argparse import ArgumentParser
from os import stat
from pwd import getpwuid
from datetime import datetime


def setup_parser():
    """Configure command line argument parser object."""

    parser = ArgumentParser(description='lists information about the paths '
                            'given in FILE.', add_help=False)
    parser.add_argument('-h', '--help', action='help', help='show this help '
                        'message and exit')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='run on sub dirs')
    parser.add_argument('files', metavar='FILE', nargs='*', default=None,
                        help='the path in which to list files')
    return parser


def get_file_owner(file):
    return getpwuid(stat(file).st_uid).pw_name


def get_file_stats(file):
    st = stat(file)
    owner = getpwuid(st.st_uid).pw_name
    permissions = st.st_mode
    mod_time = datetime.fromtimestamp(st.st_mtime)


    # I know we can make these more user friendly but for now leaving as is
    return (owner, permissions, mod_time)


def list_recursive(path):
    for subdir, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(subdir, file)
            (owner, permissions, mod_time) = get_file_stats(filepath)
            print(f'{filepath} {owner} {permissions} {mod_time}')


def list_files(paths, is_recursive=False):
    if not paths:  # use current dir
        if is_recursive:
            list_recursive('.')
        else:
            dirs = os.listdir('.')
            for file in dirs:
                (owner, permissions, mod_time) = get_file_stats(file)
                print(f'{file} {owner} {permissions} {mod_time}')

    else:  # use provided paths, one or more
        for path in paths:
            print(f'path: {path}')
            if is_recursive:
                list_recursive(path)
            else:
                # get files and dirs in path
                dirs = os.listdir(path)
                for file in dirs:
                    # need to get actual correct path,
                    # subdir was missing and file was not found
                    (owner, permissions, mod_time) = get_file_stats(
                        os.path.join(path, file))
                    print(f'{file} {owner} {permissions} {mod_time}')


def main():
    parser = setup_parser()
    args = parser.parse_args()

    if args.recursive:
        list_files(args.files, is_recursive=True)
    else:
        list_files(args.files)

    # started to implement this way then determined this is not really
    # implementing ls in python just executing the command from within
    # Left it here for discussion purposes

    # if not args.recursive:
    #     command = ['ls', '-la', args.file]
    # else:
    #     command = ['ls', '-la', '-R', args.file]

    # proc = subprocess.Popen(command, stdout=subprocess.PIPE)

    # output = proc.stdout.read()
    # output = output.decode('utf-8')
    # print(output)
    # return output


if __name__ == '__main__':
    main()
