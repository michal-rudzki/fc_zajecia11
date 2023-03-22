import sys

from package.csv_export import CSV_export
from package.json_export import JSON_export
#     0          1          2             3           4         5 
# ["in.csv", "out.csv", "0,0,gitara", "3,1,kubek", "1,2,17", "3,3,0"]

def main():
    # "in.csv", "out.pickle", "0,0,gitara", "3,1,kubek", "1,2,17", "3,3,0"
    if sys.argv[1].split('.')[1] in ['csv']:
        print(f"Input file: {sys.argv[1]}")
        file = CSV_export(sys.argv[1], sys.argv[2])
        file.export_convert()
    
    elif sys.argv[1].split('.')[1] in ['json']:
        print(f"Input file: {sys.argv[1]}")
        file = JSON_export(sys.argv[1], sys.argv[2])
        file.export_convert()

if __name__ == "__main__":
    main()