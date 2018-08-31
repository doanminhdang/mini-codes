#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 2018

@author: dang

Written for Python 2.7
Test command:
python post_processing_table.py xlsFile csvFile new_xlsFile
"""
import sys
import csv
import xlrd
import re
import Csv_Excel

text_to_move = [u'(các)',
                u'(thuộc)',
                u'(tính)',
                u'(chứng)',
                u'(có)',
                u'(bệnh)',
                u'(tật)',
                u'(sự)',
                u'(được)',
                u'(phép)',
                u'(kỹ thuật)',
                u'(nạn)',
                u'(vi khuẩn)',
                u'(để)',
                u'(cơ quan)',
                u'(hiện tượng)',
                u'(trạng thái)',
                u'(nhóm)',
                u'(bị)',
                u'(tác nhân)',
                u'(quá trình)',
                u'(con)',
                u'(hội chứng)',
                u'(có tính trạng)',
                u'(thể)',
                u'(phương pháp)',
                u'(lỗ)',
                u'(thích nghi)',
                u'(chứa)',
                u'(cơn)',
                u'(vật)',
                u'(hỗn hợp)',
                u'(tiến hoá)',
                u'(răng)',
                u'(một)',
                u'(sinh)',
                u'(đính)',
                u'(dạng)',
                u'(móng)',
                u'(kí sinh trùng)',
                u'(thuyết)',
                u'(chất)',
                u'(độ)',
                u'(bọ)',
                u'(sự, độ)'
                ]

if len(sys.argv) >= 4:
    xlsFile = str(sys.argv[1])
    csvFile = str(sys.argv[2])
    new_xlsFile = str(sys.argv[3])

reportFile = 'log.txt'

work_book = xlrd.open_workbook(xlsFile)
work_sheet = work_book.sheet_by_index(0)

report = ''

with open(csvFile, 'wb') as file_in:
        text_writer = csv.writer(file_in, delimiter='\t', quoting=csv.QUOTE_ALL)
        for rownum in range(work_sheet.nrows):
            text = work_sheet.row_values(rownum)
            for word in text_to_move:
                if re.search(re.escape(word)+r'$', text[0]):
                    text[0] = re.sub(re.escape(word)+r'$', '', text[0]).strip()
                    text[1] = word+u' '+text[1]
            text_writer.writerow(
                list(x.encode('utf-8') if type(x) == type(u'') else x
                    for x in text))
            if rownum>0 and rownum<work_sheet.nrows-2:
                this_word = work_sheet.row_values(rownum)[0]
                prev_word = work_sheet.row_values(rownum-1)[0]
                next_word = work_sheet.row_values(rownum+1)[0]
                if len(this_word)>0 and len(prev_word)>0 and len(next_word)>0:
                    if this_word[0].upper()!=prev_word[0].upper() and prev_word[0].upper()==next_word[0].upper():
                        report += 'Check 1st letter in row ' + str(rownum) + '\n'

Csv_Excel.csv_to_xls(csvFile, new_xlsFile)

with open(reportFile, 'wt') as text_file:
    text_file.write(report)
