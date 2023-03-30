import sys

from .changefile import ChangeFile
class TXT_export(ChangeFile):
    
    def __init__(self, *args):
        self.input_file = args[0]
        self.output_file = args[1] 
        self.arguments = args[2]  

    def export_convert(self):
        _read_file = self.TXT_export_read_file()
        _converted_data = self.TXT_export_change_row_col(_read_file)
        if self.output_file.split('.')[1] in ['txt']:
            self.TXT_export_save_file(_converted_data)
        else:
            self.ChangeFile_export_convert(_converted_data, self.output_file, self.input_file)
    
    def TXT_export_read_file(self):
        content_file = []
        with open(self.input_file, mode='r') as txtfile:
            content_file.append(txtfile.read())
        content_file = content_file[0].split('\n')
        return content_file
        
    def TXT_export_change_row_col(self, file_content):
        print("Output file: ", self.output_file)
        print("Arguments: ", self.arguments)
        output_txt = []
        cli_arg = self.arguments
        while len(file_content) != 0:
            output_txt.append(file_content[0:4])
            file_content = file_content[4:]

        while len(cli_arg) != 0:
            row = int(cli_arg[0].split(',')[0])
            col = int(cli_arg[0].split(',')[1])
            val = cli_arg[0].split(',')[2]
            output_txt[col][row] = val
            cli_arg = cli_arg[1:]
        return output_txt
    
    def TXT_export_save_file(self, data_to_save):
        with open(self.output_file, mode = 'w') as txtFile:
            for data in data_to_save:
                for read_data in data:
                    txtFile.write(read_data+"\n")