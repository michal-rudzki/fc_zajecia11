import json
import sys

from .changefile import ChangeFile
class JSON_export(ChangeFile):
    
    def __init__(self, *args):
        self.input_file = args[0]
        self.output_file = args[1] 
        self.arguments = args[2]
    
    def export_convert(self):
        _read_file = self.JSON_export_read_file()
        _converted_data = self.JSON_export_change_row_col(_read_file)
        if self.output_file.split('.')[1] in ['json']:
            self.JSON_export_save_file(_converted_data)
        else:
            self.ChangeFile_export_convert(_converted_data, self.output_file, self.input_file)
        
    def JSON_export_read_file(self):
        content_file = []
        with open(self.input_file, mode='r') as jsonfile:
            content_file = json.load(jsonfile)
        return content_file
    
    def JSON_export_change_row_col(self, file_content):
        print("Output file: ", self.output_file)
        print("Arguments: ", self.arguments)
        output_json = file_content
        for count in range(len(sys.argv[3:])):
            row = int(self.arguments[count].split(',')[0])
            col = int(self.arguments[count].split(',')[1])
            val = self.arguments[count].split(',')[2]
            output_json[str(col)][row] = val
        return output_json
        
    def JSON_export_save_file(self, data_to_save):
        with open(self.output_file, mode='w') as jsonfile:
            json.dump(data_to_save, jsonfile, indent=4)