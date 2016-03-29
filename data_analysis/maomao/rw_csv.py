import sys
import csv
from os import listdir, remove, rename
from os.path import isfile, isdir, join

def process_csv(folder):
    for f in listdir(folder):
        path = join(folder, f)
        tmp_path = join(folder, "tmp.CSV")
        if isfile(path) and f.endswith(".CSV"):
            with open(path, "r", encoding="big5", errors="ignore") as f_read:
                csv_read = csv.reader(f_read)
                with open(tmp_path, "w") as f_write:
                    csv_write = csv.writer(f_write)
                    csv_write.writerows(csv_read)
            remove(path)
            rename(tmp_path, path)

def main():
    if len(sys.argv) != 2 or (not isdir(sys.argv[1])):
        print("Usage: python3 rw_csv.py Path://CSV_Folder")
        return

    process_csv(sys.argv[1])

if __name__ == "__main__":
    main()