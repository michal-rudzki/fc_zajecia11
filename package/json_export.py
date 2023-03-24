import json
import sys

from .changefile import ChangeFile
class JSON_export(ChangeFile):
    
    def __init__(self, *args):
        self.input_file = sys.argv[1]
        self.output_file = sys.argv[2]
    
    def export_convert(self):
        _read_file = self.JSON_export_read_file()
        _converted_data = self.JSON_export_change_row_col(_read_file)
        if sys.argv[2].split('.')[1] in ['json']:
            self.JSON_export_save_file(_converted_data)
        else:
            self.ChangeFile_export_convert(_converted_data, self.output_file, self.input_file)
        
    def JSON_export_read_file(self):
        content_file = []
        with open(self.input_file, mode='r') as jsonfile:
            content_file = json.load(jsonfile)
        return content_file
    
    def JSON_export_change_row_col(self, file_content):
        print("Output file: ", sys.argv[2])
        print("Arguments: ", sys.argv[3:])
        output_json = file_content
        for count in range(len(sys.argv[3:])):
            row = int(sys.argv[3:][count].split(',')[0])
            col = int(sys.argv[3:][count].split(',')[1])
            val = sys.argv[3:][count].split(',')[2]
            output_json[str(col)][row] = val
        return output_json
        
    def JSON_export_save_file(self, data_to_save):
        with open(sys.argv[2], mode='w') as jsonfile:
            json.dump(data_to_save, jsonfile, indent=4)