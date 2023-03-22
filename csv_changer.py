import sys
from package.changefile import ChangeFile
from package.csv_export import CSV_export
#     0          1          2             3           4         5 
# ["in.csv", "out.csv", "0,0,gitara", "3,1,kubek", "1,2,17", "3,3,0"]

def main():
    # "in.csv", "out.pickle", "0,0,gitara", "3,1,kubek", "1,2,17", "3,3,0"
    file = ChangeFile(sys.argv[1], sys.argv[2])
    content = file.load_file()
    output_content = file.set_col_row_change(sys.argv[3:], content)
    file.save_file(sys.argv[2], output_content)

if __name__ == "__main__":
    main()