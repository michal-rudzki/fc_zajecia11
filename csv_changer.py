import csv
import sys
from modules import FileExport

class ChangeFile(FileExport):

    def __init__(self, *args):
        self.input_file = args[0]
        self.output_file = args[1]
    
    def load_file(self):
        content_file = []
        with open(self.input_file, mode = 'r', newline = '') as csvfile:
            file = csv.reader(csvfile, delimiter = ' ')
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
                
    #def save_file(self, csv_file, csv_output_content):
    #    with open(csv_file, mode = 'w', newline = '') as csvfile:
    #        writer = csv.writer(csvfile)
    #        writer.writerows(csv_output_content)

#     0          1          2             3           4         5 
# ["in.csv", "out.csv", "0,0,gitara", "3,1,kubek", "1,2,17", "3,3,0"]
def main():
    file = ChangeFile(sys.argv[1], sys.argv[2])
    csv_content = file.load_file()
    csv_output_content = file.set_col_row_change(sys.argv[3:], csv_content)
    file.save_file(sys.argv[2], csv_output_content)


if __name__ == "__main__":
    main()