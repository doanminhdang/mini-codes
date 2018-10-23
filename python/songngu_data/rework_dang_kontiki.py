#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Reflow text from pdftotext to non-segmented-paragraph text.

Created on Tue Oct 23 2018

@author: dang

Example: (remember to put file names with space in double quote)
python rework_dang_kontiki.py text_kontiki_en.txt Kon_Tiki_en.txt
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
result_file = str(sys.argv[2])

with open(source_file,'rt') as text_file:
    text = text_file.read().decode('utf-8')

#print('Replacing special characters...')
#for k in range(len(search_series)):
    #text = text.replace(search_series[k], replace_series[k])

#print('Removing page numbers...')
#page_number_pattern = r'(\s{2,}[0-9]+\/203\s{2,})'
#text = re.sub(page_number_pattern, ' ', text)


print('Remove page breaks which are 4-consecutive blank lines...')
text = text.replace('\n\n\n\n', '')


print('Re-joining sentences by deleting unnecessary line breaks...')
replace_pattern = r'([^\n\s])\s\n(.)'
text = re.sub(replace_pattern, '\g<1> \g<2>', text)

with open(result_file,'wt') as new_text_file:
    new_text_file.write(text.encode('utf-8'))
    #new_text_file.write('')
print('Done')
