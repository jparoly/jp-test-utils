#!/usr/bin/python3
import unittest
import subprocess


class MiniGrepTests(unittest.TestCase):

    def test_grep_file_one_line(self):
        output = subprocess.getoutput(
            './mini_grep.py -e test test_file.txt')
        self.assertIn('3 this is a test', output)

    def test_grep_file_multiple_lines(self):
        output = subprocess.getoutput(
            './mini_grep.py -e test test_2_lines.txt')
        self.assertIn('1 how about them tests', output)
        self.assertIn('4 testing is good', output)

    def test_grep_file_no_line_number(self):
        output = subprocess.getoutput(
            './mini_grep.py -e test test_2_lines.txt -q')
        self.assertIn('how about them tests', output)
        self.assertIn('testing is good', output)

    def test_grep_file_no_match(self):
        output = subprocess.getoutput(
            './mini_grep.py -e nada test_2_lines.txt -q')
        self.assertNotIn('nada', output)

    def test_grep_files_two_files(self):
        output = subprocess.getoutput(
            './mini_grep.py -e test test_2_lines.txt test_file.txt')
        self.assertIn('1 how about them tests', output)
        self.assertIn('4 testing is good', output)
        self.assertIn('3 this is a test', output)


if __name__ == '__main__':
    unittest.main()
