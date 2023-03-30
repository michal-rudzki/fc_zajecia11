import csv
import sys

from .changefile import ChangeFile
class CSV_export(ChangeFile):
    
    def __init__(self, *args):
        self.input_file = args[0]
        self.output_file = args[1]
        self.arguments = args[2]
    
    def export_convert(self):
        _read_file = self.CSV_export_read_file()
        _converted_data = self.CSV_export_change_row_col(_read_file)
        if self.output_file.split('.')[1] in ['csv']:
            self.CSV_export_save_file(_converted_data)
        else:
            self.ChangeFile_export_convert(_converted_data, self.output_file, self.input_file)
    
    def CSV_export_read_file(self):
        content_file = []
        with open(self.input_file, mode='r', newline='') as csvfile:
            file = csv.reader(csvfile, delimiter=' ')
            for read_file in file:
                content_file.append(read_file)
        return content_file
    
    def CSV_export_change_row_col(self, file_content):
        print("Output file: ", self.output_file)
        print("Arguments: ", self.arguments)
        cli_args = self.arguments
        tmp = []
        output_csv = []
        for count in range(len(cli_args)):
            row = int(cli_args[count].split(',')[0])
            col = int(cli_args[count].split(',')[1])
            val = cli_args[count].split(',')[2]
            tmp.append(file_content[int(col)][0])
            if count == col:
                t = tmp[col].split(',')
                t[row] = val
                output_csv.append(t)
        return output_csv
    
    def CSV_export_save_file(self, data_to_save):
        with open(self.output_file, mode = 'w', newline = '') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data_to_save)