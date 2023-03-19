import sys
from package.changefile import ChangeFile
#     0          1          2             3           4         5 
# ["in.csv", "out.csv", "0,0,gitara", "3,1,kubek", "1,2,17", "3,3,0"]
def main():
    file = ChangeFile(sys.argv[1], sys.argv[2])
    csv_content = file.load_file()
    csv_output_content = file.set_col_row_change(sys.argv[3:], csv_content)
    file.save_file(sys.argv[2], csv_output_content)


if __name__ == "__main__":
    main()