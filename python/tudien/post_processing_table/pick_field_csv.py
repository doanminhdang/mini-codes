#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 2018

@author: dang

Written for Python 2.7
Test command:
python pick_field_csv.py csvFile new_csvFile xlsFile
"""
import sys
import csv
import xlrd
import re
import Csv_Excel

metaFile = 'meta_KHCN_DAV.csv'
colnum = 2
text_to_pick_utf8 = [u'ĐIỆN',
                u'KT_ĐIỆN',
                u'Đ_TỬ',
                u'Q_HỌC',
                u'V_LÝ',
                u'VLB_XẠ',
                u'VLC_LỎNG',
                u'VLD_ĐỘNG',
                u'VLHC_BẢN',
                u'Đ_KHIỂN',
                u'Đ_LƯỜNG',
                u'ÂM',
                u'CNH_NHÂN',
                u'ĐL&ĐK',
                u'KTH_NHÂN'
                ]

text_to_pick = [word.encode('utf-8') for word in text_to_pick_utf8]


def pick_from_csv(csvFile, colnum, text_to_pick, reportFile = 'log.txt'):
    new_table = []
    num_words = 0
    with open(csvFile, 'rt') as file_in:
        text_reader = csv.reader(file_in, delimiter='\t')
        for r, row in enumerate(text_reader):
            pick_flag = False
            for word in text_to_pick:
                if len(row)>colnum and re.search(re.escape(word), row[colnum]):
                    pick_flag = True
            if pick_flag:
                num_words += 1
                new_table.append(row)
    report = 'Total number of words extracted: '+str(num_words)
    print(report)
    with open(reportFile, 'wt') as text_file:
        text_file.write(report)
    return new_table

def write_table_csv(exportFile, table):
    with open(exportFile, 'wt') as csvfile:
        textWriter = csv.writer(csvfile, delimiter='\t')
        for i in range(len(table)):
            textWriter.writerow(table[i])

def add_meta_info(csvFile, metaFile):
    with open(metaFile, 'rt') as file_in:
        meta_lines = file_in.read()
    with open(csvFile, 'rt') as file_in:
        csv_lines = file_in.read()
    new_text = meta_lines+csv_lines
    with open(csvFile, 'wt') as file_out:
        file_out.write(new_text) 

def pick_field_csv(csvFile, colnum, text_to_pick, new_csvFile, xlsFile):
    table = pick_from_csv(csvFile, colnum, text_to_pick)
    write_table_csv(new_csvFile, table)
    add_meta_info(new_csvFile, metaFile)
    Csv_Excel.csv_to_xls(new_csvFile, xlsFile)

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        csvFile = str(sys.argv[1])
        new_csvFile = str(sys.argv[2])
        xlsFile = str(sys.argv[3])
        pick_field_csv(csvFile, colnum, text_to_pick, new_csvFile, xlsFile)
    else:
        print('python pick_field_csv.py csvFile new_csvFile xlsFile')

