import pickle
import sys

from .changefile import ChangeFile

class PICKLE_export(ChangeFile):
    
    def __init__(self, *args):
        self.input_file = sys.argv[1]
        self.output_file = sys.argv[2]
    
    def export_convert(self):
        _read_file = self.PICKLE_export_read_file()
        _converted_data = self.PICKLE_export_change_row_col(_read_file)
        if sys.argv[2].split('.')[1] in ['pickle']:
            self.PICKLE_export_save_file(_converted_data)
        else:
            self.ChangeFile_export_convert(_converted_data, self.output_file, self.input_file)
    
    def PICKLE_export_read_file(self):
        content_file = []
        with open(self.input_file, mode='rb') as picklefile:
            content_file = pickle.load(picklefile)
        return content_file
    
    def PICKLE_export_change_row_col(self, file_content):
        print("Output file: ", sys.argv[2])
        print("Arguments: ", sys.argv[3:])
        cli_args = sys.argv[3:]
        tmp = []
        output_pickle = []
        for count in range(len(cli_args)):
            row = int(cli_args[count].split(',')[0])
            col = int(cli_args[count].split(',')[1])
            val = cli_args[count].split(',')[2]
            file_content[col][row] = val
        output_pickle = file_content
        return output_pickle

    def PICKLE_export_save_file(self, data_to_save):
        with open(sys.argv[2], mode='wb') as pickleFile:
            pickle.dump(data_to_save, pickleFile)