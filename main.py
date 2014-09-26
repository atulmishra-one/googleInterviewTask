##########################################
#@author : atulmishra.one@gmail.com
#
#@description : This program takes a CSV file 
# and generate the companies share report
# according to year and month
#
##########################################

import csv
import sys
import os
from __builtin__ import next, map
from collections import OrderedDict

#E:\Python27\workspace\googleInterviewTask\test_shares_data.csv
class ShareReport(object):
    
    output = OrderedDict()
    result = None
    
    def __init__(self, file_path=None):
        if not file_path:
            self.file_path = raw_input("\n Enter CSV File path : ")
        else:
            self.file_path = file_path
            
        ext = os.path.splitext(self.file_path)[1]
        
        """ Accept CSV file only. """
        
        if ext != '.csv':
            print 'Invalid file extension.'
            sys.exit(0)
        
        """ Parse and extract The Csv file Data. """
        self.parse_csv_file()
        
    def parse_csv_file(self):
        
        with open(self.file_path, "rb", 1) as csv_file:
            dialect = csv.Sniffer().sniff(csv_file.read(1024))
            has_header = csv.Sniffer().has_header(csv_file.read(1024))
            csv_file.seek(0)
            
            if not has_header:
                raise Exception('Not a correct CSV file')
            
            csv_data = csv.reader(csv_file, dialect)
            
            company_names = next(csv_data)[2:] # Extract the Companies name
            
            for name in company_names:
                self.output[name] = {'price': 0, 'year': 'year', 'month': 'month'}
            for row in csv_data:
                year, month = row[:2]
                for name, price in zip(company_names, map(int, row[2:])):
                    if self.output[name]['price'] < price:
                        self.output[name] = {'price':price, 'year': year, 'month': month}
            
            self.result = '\nCompany name\tYear\tMonth\tMax Price\n\n'
            for company_name , analysis_dict in self.output.items():
                self.result += '%s\t%s\t%s\t%d\n' % (company_name, analysis_dict['year'], analysis_dict['month'], analysis_dict['price'])
                
    def generate(self):
        """ Generate output . """
        return self.result
            
                        
            


if __name__ == "__main__":
    """ Print the Report. """
    report = ShareReport()
    sys.exit(report.generate())            
    
