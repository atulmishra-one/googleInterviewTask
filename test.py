###################################################
#@author : atulmishra.one@gmail.com
#
#@description : This is Test class for main program. 
#
####################################################

import unittest
import os
import random
import csv
from main import ShareReport
from __builtin__ import range, str


class RandomCSVFile(unittest.TestCase):
    
    """ Class to generate random csv files. Best for testing files """
    
    def setUp(self):
        self.start_year = random.randint(1990, 2000)
        self.end_year   = random.randint(2001, 2013)
        self.years = range(self.start_year, self.end_year)
        self.months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.share_values = range(100, 1000)
        self.companies_number = random.randint(0, 5)  #Random Company Number.
        self.number_of_entries = (self.end_year - self.start_year) * 1
        self.csv_header = ['Year', 'Month']
        self.test_dict = dict()
        
        for i in range(self.companies_number):
            self.csv_header.append('Comp%s'% str(i+1))
            self.test_dict['Comp%s' % str(i + 1)] = {'price': 0, 'year': 'year', 'month': 'month'}
        with open('test.csv', 'wb') as csv_file:
            data_writer = csv.writer(csv_file, csv.excel)
            data_writer.writerow(self.csv_header)
            
            year = self.start_year
            while year <= self.end_year:
                for i in self.months:
                    data_row = [year, i]
                    for j in range(self.companies_number):
                        share_val = random.choice(self.share_values)
                        data_row.append(share_val)
                        if self.test_dict['Comp%s' % str(j + 1)]['price'] < share_val:
                            self.test_dict['Comp%s' % str(j + 1)] = {'price': share_val, 'year': year, 'month': i}
                    data_writer.writerow(data_row)
            year += 1
            
            self.csv_rand_input = 'test.csv'
   
class InvalidFileExtension(RandomCSVFile):
    """ This check for csv file extension only """
    def test_invalid_file_ext(self):
        ext = os.path.splitext(self.csv_rand_input)[1]
        self.assertEqual(ext, '.csv')
     
class ValidateOutput(RandomCSVFile):
    def test_output(self):
        report = ShareReport(self.csv_rand_input)
        result = report.generate()
        self.assertTrue(not 'Critical' in result)
        for key in report.output:
            self.assertTrue(key in result)
        
if __name__ == "__main__":
    unittest.main()