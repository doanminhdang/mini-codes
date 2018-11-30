#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

def pdf_split(filename_base, first_page, last_page, length_item):
    """
    Counting from first_page to last_page, split into small PDF files of length_item pages, use pdftk
    """
    mainname, extname = os.path.splitext(filename_base)  # mainname is '123', extname is '.pdf'
    print('Start to split the file '+filename_base)
    for start_page in range(first_page, last_page, length_item):
        end_page = start_page + length_item - 1
        newfilename = mainname + '_' + str(start_page) + '-' + str(end_page) + extname
        os.system('pdftk '+filename_base+' cat '+str(start_page)+'-'+str(end_page)+' output '+newfilename)
        print('File ' + newfilename + ' created in the same directory with ' + filename_base)
    print('Finished splitting the file '+filename_base)

if __name__ == "__main__":
    filename_base = str(sys.argv[1])
    first_page = int(sys.argv[2])
    last_page = int(sys.argv[3])
    length_item = int(sys.argv[4])
    pdf_split(filename_base, first_page, last_page, length_item)
