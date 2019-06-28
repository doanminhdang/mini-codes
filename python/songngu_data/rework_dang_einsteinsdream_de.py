#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Transform PDF to non-segmented-paragraph text.

Created on Tue Aug 28 2018

@author: dang

Example: (remember to put file names with space in double quote)
python pdf2txt_dang.py "A.\ Lightman\ -\ Einstein\'s\ Dreams.pdf" Einstein_Dreams.txt
"""

import sys
import os
import re

search_series = [u'â', 
                 u'â',
                 u'â',
                 u'â¢',
                 u'ÃŒ']
replace_series = [u'’',
                  u'“',
                  u'”',
                  u'•',
                  u'ü']

source_file = str(sys.argv[1])
if len(sys.argv) >= 3:
    result_file = str(sys.argv[2])

convert_command = 'pdftotext ' + source_file + ' ' + result_file
print(convert_command)
os.system(convert_command)

with open(result_file,'rt') as text_file:
    text = text_file.read().decode('utf-8')

print('Replacing special characters...')
for k in range(len(search_series)):
    text = text.replace(search_series[k], replace_series[k])

#print('Removing page numbers...')
#page_number_pattern = r'(\s{2,}[0-9]+\/203\s{2,})'
#text = re.sub(page_number_pattern, ' ', text)

print('Correcting diary dates...')
date_pattern = r'(\d+) *\.\s+([A-Z]+)\s+([I1]9[O0]5)'
text = re.sub(date_pattern, '* \g<1>. \g<2> 1905', text)

print('Re-joining sentences by deleting unnecessary line breaks...')
replace_pattern = r'([^\.\d\n])\n+(.)'
text = re.sub(replace_pattern, '\g<1> \g<2>', text)

with open(result_file,'wt') as new_text_file:
    new_text_file.write(text.encode('utf-8'))
print('Done')
