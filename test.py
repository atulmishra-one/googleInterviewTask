###################################################
#@author : atulmishra.one@gmail.com
#
#@description : This is Test class for main program. 
#
####################################################

import unittest
import os
import csv
from main import ShareReport


class CSVTestCase(unittest.TestCase):
    file_path = r'E:\Python27\workspace\googleInterviewTask\test_shares_data.csv'
    pass

class FileExits(CSVTestCase):
    def test_file_exits(self):
        exits = os.path.exists(self.file_path)
        self.assertTrue(exits)
        
class ValidCSVContent(CSVTestCase):
    
    def test_header_of_csv(self):
        """ Test if csv file has headers. """
        with open(self.file_path, "rb", 1) as csv_file:
            has_header = csv.Sniffer().has_header(csv_file.read(1024))
            self.assertTrue(has_header)
            csv_file.seek(0)
    def test_has_content(self):
        """ False means a non-empty file. """
        has_content = os.stat(self.file_path).st_size > 0
        self.assertTrue(has_content)

class InvalidFileExtension(CSVTestCase):
    """ This check for csv file extension only """
    def test_invalid_file_ext(self):
        ext = os.path.splitext(self.file_path)[1]
        self.assertEqual(ext, '.csv')
     
class ValidateOutput(CSVTestCase):
    def test_output(self):
        report = ShareReport(self.file_path)
        result = report.generate()
        self.assertTrue(not 'Critical' in result)
        for key in report.output:
            self.assertTrue(key in result)
            

        
if __name__ == "__main__":
    unittest.main()