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

metaFile = 'meta_TD_TSan_FAO_AV.csv'

def remove_duplicate_space(text):
    new_text = re.sub(r" {2,}", " ", text)
    return new_text

def strict_hyphen(text):
    new_text = re.sub(r" *- *", "-", text)
    return new_text

def remove_first_capital(text1, text2):
    capital_words_t1 = re.findall(r"[A-Z]\S+\b", text1)
    capital_words_t2 = re.findall(r"^[A-Z]\S+\b", text2)
    if len(capital_words_t1)>0 and not capital_words_t1[0].isupper() and capital_words_t1[0] not in text2:
        # donot change abbreviation like: CIF (...)
        # also donot change: Social Impact Assessment
        #   but change: Assessment, social impact- (SIA)
        if len(capital_words_t1)==1 or capital_words_t1[1].isupper():
            text1 = text1[0].lower() + text1[1:]
    if len(capital_words_t2)>0 and capital_words_t2[0] not in text1:
        text2 = text2[0].lower() + text2[1:]

    capital_vietnamese='ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÉÈẺẼẸÊẾỀỂỄỆĐÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ'.decode('utf-8')
    lower_vietnamese  ='áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệđíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ'.decode('utf-8')
    if text2.decode('utf-8')[0] in capital_vietnamese:
        #text2 = lower_vietnamese[capital_vietnamese.find(text2[0])] + text2[1:]
        text2 = (lower_vietnamese[capital_vietnamese.find(text2.decode('utf-8')[0])]+text2.decode('utf-8')[1:]).encode('utf-8')
    return text1, text2

def rearrange_td_thuysan_csv(csvFile, reportFile = 'log.txt'):
    new_table = []
    num_words = 0
    current_main_term = ''
    with open(csvFile, 'rt') as file_in:
        text_reader = csv.reader(file_in, delimiter='\t')
        for r, row in enumerate(text_reader):
            # rows with even id: 0, 2,... are terms
            # rows with odd id: 1, 3,... are explanations
            if r%2==0:
                en_word = row[1]
                vi_word = row[2]
                en_word, vi_word = remove_first_capital(en_word, vi_word)
                # rearrange for such case: adaptation, livelihood-
                # or such case: solids, total dissolved- (TDS)
                en_word = re.sub(r"^(.+), *(.+)-(.*)$", r"\2 \1\3", en_word)
            else:
                explanation_vi = row[1]
                # then write the whole entry
                new_table.append([en_word, vi_word, explanation_vi])
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

def process_td_thuysan(csvFile, new_csvFile, xlsFile):
    table = rearrange_td_thuysan_csv(csvFile)
    write_table_csv(new_csvFile, table)
    add_meta_info(new_csvFile, metaFile)
    Csv_Excel.csv_to_xls(new_csvFile, xlsFile)

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        csvFile = str(sys.argv[1])
        new_csvFile = str(sys.argv[2])
        xlsFile = str(sys.argv[3])
        process_td_thuysan(csvFile, new_csvFile, xlsFile)
    else:
        print('python process_td_thuysan.py csvFile new_csvFile xlsFile')
