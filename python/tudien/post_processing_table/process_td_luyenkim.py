#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 2018

@author: dang

Written for Python 2.7
"""
import sys
import os
import csv
import xlrd
import re
import Csv_Excel

metaFile = 'meta_LK_AV.csv'

def remove_duplicate_space(text):
    new_text = re.sub(r" {2,}", " ", text)
    return new_text

def strict_hyphen(text):
    new_text = re.sub(r" *- *", "-", text)
    return new_text

def process_luyenkim_csv(csvFile, reportFile = 'log.txt'):
    new_table = []
    num_words = 0
    current_main_term = ''
    with open(csvFile, 'rt') as file_in:
        text_reader = csv.reader(file_in, delimiter='\t')
        for r, row in enumerate(text_reader):
            # process based on english column
            en_word = strict_hyphen(remove_duplicate_space(row[0]))
            vi_word = strict_hyphen(remove_duplicate_space(row[1]))
            if re.search(r"~", en_word):
                en_word = re.sub(r"~", current_main_term, en_word)
            else:
                # update the current_main_term by this word
                current_main_term = en_word
            new_table.append([en_word, vi_word])
    #report = 'Total number of words extracted: '+str(num_words)
    #print(report)
    #with open(reportFile, 'wt') as text_file:
        #text_file.write(report)
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

def batch_process_td_luyenkim(source_dir, new_csvFile, xlsFile):
    combined_table = []
    for (dirname, dirs, files) in os.walk(source_dir):
        for filename in sorted(files):
            filename_main, file_extension = os.path.splitext(filename)
            print(filename_main, file_extension)
            if file_extension == '.csv':
                csv_file = os.path.join(dirname,filename)
                new_sub_table = process_luyenkim_csv(csv_file)
                combined_table.extend(new_sub_table)
    write_table_csv(new_csvFile, combined_table)
    add_meta_info(new_csvFile, metaFile)
    Csv_Excel.csv_to_xls(new_csvFile, xlsFile)

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        source_dir = str(sys.argv[1])
        new_csvFile = str(sys.argv[2])
        xlsFile = str(sys.argv[3])
        batch_process_td_luyenkim(source_dir, new_csvFile, xlsFile)
    else:
        print('python process_td_luyenkim.py source_dir new_csvFile xlsFile')
