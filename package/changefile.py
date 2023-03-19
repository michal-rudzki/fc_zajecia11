import csv
import json
import pickle
from .fileexport import FileExport

class ChangeFile(FileExport):

    def __init__(self, *args):
        self.input_file = args[0]
        self.output_file = args[1]

    def load_file(self):
        content_file = []
        with open(self.input_file, mode='r', newline='') as csvfile:
            file = csv.reader(csvfile, delimiter=' ')
            for read_file in file:
                content_file.append(read_file)
        return content_file

    def set_col_row_change(self, cli_args, csv_in_file):
        tmp = []
        output_csv = []
        for count in range(len(cli_args)):
            row = int(cli_args[count].split(',')[0])
            col = int(cli_args[count].split(',')[1])
            val = cli_args[count].split(',')[2]
            tmp.append(csv_in_file[int(col)][0])
            if count == col:
                t = tmp[col].split(',')
                t[row] = val
                output_csv.append(t)
        return output_csv
