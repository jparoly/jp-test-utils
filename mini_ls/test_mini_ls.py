#!/usr/bin/python3
import unittest
import subprocess
from datetime import datetime


class MiniLsTests(unittest.TestCase):

    def test_ls_current_dir_not_recursive(self):
        output = subprocess.getoutput('./mini_ls.py')
        self.assertIn('test_mini_ls.py', output)
        self.assertIn('mini_ls.py', output)
        self.assertIn('test_paths_2', output)
        self.assertIn('README.md', output)
        self.assertIn('test_paths_1', output)
        self.assertIn('33261', output)  # permissions
        self.assertIn('16877', output)  # permissions
        self.assertIn('jparoly', output)
        self.assertNotIn('test_paths_2_1', output)
        self.assertNotIn('test2_2.txt', output)
        self.assertNotIn('test2_1_1.txt', output)

        # assert today's date is in output
        # recognize if not modified today it will fail
        # Can parse out date from string, turn to datetime
        # object and validate there is a datetime present
        # TODO: harden test for modified time
        # idea: in test edit file, then check for today's date

        self.assertIn(datetime.today().strftime('%Y-%m-%d'), output)

    def test_current_dir_recursive(self):
        output = subprocess.getoutput('./mini_ls.py -r')
        self.assertIn('test_paths_2_1', output)
        self.assertIn('test2_2.txt', output)
        self.assertIn('test2_1_1.txt', output)

    def test_one_path_not_recursive(self):
        output = subprocess.getoutput('./mini_ls.py test_paths_1')
        self.assertIn('test_paths_1', output)
        self.assertIn('test1_2.txt', output)
        self.assertIn('test1_1.txt', output)

    def test_one_path_recursive(self):
        output = subprocess.getoutput('./mini_ls.py test_paths_2 -r')
        self.assertNotIn('test_paths_1', output)
        self.assertIn('test_paths_2_1', output)
        self.assertIn('test2_1_1.txt', output)
        self.assertIn('test2_1.txt', output)
        self.assertIn('test2_2.txt', output)

    def test_two_paths_not_recursive(self):
        output = subprocess.getoutput('./mini_ls.py test_paths_2 test_paths_1')
        self.assertIn('test_paths_1', output)
        self.assertIn('test1_2.txt', output)
        self.assertIn('test1_1.txt', output)
        self.assertIn('test2_1.txt', output)
        self.assertIn('test2_2.txt', output)
        self.assertNotIn('test2_1_1.txt', output)

    def test_two_paths_recursive(self):
        output = subprocess.getoutput(
            './mini_ls.py test_paths_2 test_paths_1 -r')
        self.assertIn('test_paths_1', output)
        self.assertIn('test1_2.txt', output)
        self.assertIn('test1_1.txt', output)
        self.assertIn('test2_1.txt', output)
        self.assertIn('test2_2.txt', output)
        self.assertIn('test2_1_1.txt', output)


if __name__ == '__main__':
    unittest.main()
