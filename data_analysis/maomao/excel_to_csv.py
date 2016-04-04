import sys
import csv
import xlrd
from os.path import isfile, join

def process_excel(file):
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheets()[0]

    tmp_file = join(file.rsplit("/", maxsplit=1)[0], "test.csv")
    with open(tmp_file,"w") as f:
        w = csv.writer(f)
        for i in range(sheet.nrows):
            w.writerow(sheet.row_values(i))

def main():
    if len(sys.argv) != 2 or (not isfile(sys.argv[1])) or (not (sys.argv[1].endswith(".xls") or sys.argv[1].endswith(".xlsx"))):
        print("Usage: python3 excel_to_csv.py Path://EXCEL_FILE")
        return

    process_excel(sys.argv[1])

if __name__ == "__main__":
    main()