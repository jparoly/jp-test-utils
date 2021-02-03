#!/usr/bin/python3
import unittest
from mini_grep import grep_file
from mini_grep import grep_files


class MiniGrepTests(unittest.TestCase):

    def test_grep_file_one_line(self):
        self.assertEqual(
            grep_file('test', 'test_file.txt', True),
            ['3 this is a test']
        )

    def test_grep_file_multiple_lines(self):
        self.assertEqual(
            grep_file('test', 'test_2_lines.txt', True),
            ['1 how about them tests', '4 testing is good']
        )

    def test_grep_file_no_line_number(self):
        self.assertEqual(
            grep_file('test', 'test_2_lines.txt', print_lineno=False),
            ['how about them tests', 'testing is good']
        )

    def test_grep_file_no_match(self):
        self.assertEqual(
            grep_file('nada', 'test_2_lines.txt', print_lineno=False),
            []
        )

    def test_grep_files_two_files(self):
        self.assertEqual(
            grep_files('test', ['test_2_lines.txt', 'test_file.txt'],
                       print_lineno=True),
            [['1 how about them tests', '4 testing is good'],
             ['3 this is a test']]
        )


if __name__ == '__main__':
    unittest.main()
