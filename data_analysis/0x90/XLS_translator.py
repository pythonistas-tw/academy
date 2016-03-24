#!/usr/bin/env python
# encoding: utf-8

import xlrd
import csv
import os


def singel_file(source_file):
    data = xlrd.open_workbook(source_file)
    table = data.sheets()[0]
    with open(os.path.splitext(os.path.basename(source_file))[0] + '.csv',
              'w', newline='') as csvfile:
        spanwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in range(table.nrows):
            csv_list = []
            for col in range(table.ncols):
                csv_list.append(table.cell(row, col).value)
            spanwriter.writerow(csv_list)

singel_file('EXCEL1.xls')
