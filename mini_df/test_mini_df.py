#!/usr/bin/python3
import unittest
import subprocess


class MiniDfTests(unittest.TestCase):

    def test_df_no_path(self):
        output = subprocess.getoutput('./mini_df.py')
        self.assertIn('current path', output)
        self.assertIn('total=', output)
        self.assertIn('used=', output)
        self.assertIn('free=', output)
        self.assertNotIn('Capacity', output)

    def test_df_no_path_pretty(self):
        output = subprocess.getoutput('./mini_df.py -h')
        self.assertIn('Disk Usage for the Current Path', output)
        self.assertIn('Total Disk Space', output)
        self.assertIn('Used Disk Space', output)
        self.assertIn('Free Disk Space', output)
        self.assertNotIn('total=', output)
        self.assertNotIn('used=', output)
        self.assertNotIn('free=', output)

    def test_df_one_path(self):
        output = subprocess.getoutput('./mini_df.py /System/')
        self.assertNotIn('current path', output)
        self.assertIn('total=', output)
        self.assertIn('used=', output)
        self.assertIn('free=', output)
        self.assertNotIn('Capacity', output)
        self.assertIn('/System/', output)

    def test_df_one_path_pretty(self):
        output = subprocess.getoutput('./mini_df.py -h /System/')
        self.assertNotIn('current path', output)
        self.assertIn('Disk Usage for "/System/"', output)
        self.assertIn('Total Disk Space', output)
        self.assertIn('Used Disk Space', output)
        self.assertIn('Free Disk Space', output)
        self.assertNotIn('total=', output)
        self.assertNotIn('used=', output)
        self.assertNotIn('free=', output)

    def test_df_two_paths(self):
        output = subprocess.getoutput('./mini_df.py /System/ /Volumes/')
        self.assertNotIn('current path', output)
        self.assertIn('total=', output)
        self.assertIn('used=', output)
        self.assertIn('free=', output)
        self.assertIn('/System/', output)
        self.assertIn('/Volumes/', output)
        self.assertNotIn('Capacity', output)

    def test_df_two_paths_pretty(self):
        output = subprocess.getoutput('./mini_df.py -h /System/ /Volumes/')
        self.assertNotIn('current path', output)
        self.assertIn('Disk Usage for "/System/"', output)
        self.assertIn('Disk Usage for "/Volumes/"', output)
        self.assertIn('Total Disk Space', output)
        self.assertIn('Used Disk Space', output)
        self.assertIn('Free Disk Space', output)
        self.assertNotIn('total=', output)
        self.assertNotIn('used=', output)
        self.assertNotIn('free=', output)

    # TODO: Add test to make sure there are two occurences of certain strings
    # when providing two paths

    def test_bad_path(self):
        output = subprocess.getoutput(
            './mini_df.py bad_path')
        self.assertIn('Please provide a valid path', output)


if __name__ == '__main__':
    unittest.main()
