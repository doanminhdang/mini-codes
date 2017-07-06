#!/usr/bin/env python
# Script to extract titles of papers in the program of IFAC World Congress 2017
# Usage: download the source files from IFAC World Congress website, put them
#   in the same directory with this script. Sources files are at:
#   https://ifac.papercept.net/conferences/conferences/IFAC17/program/IFAC17_ContentListWeb_1.html
#   till
#   https://ifac.papercept.net/conferences/conferences/IFAC17/program/IFAC17_ContentListWeb_5.html
#   Edit this python script to input data in the raw_list and keyword, then run:
#     python ifac_crawl.py
#   The list will be extracted as a CSV file.
# IFAC WC 2017 has the listing of which papers have which keywords:
#   https://ifac.papercept.net/conferences/conferences/IFAC17/program/IFAC17_KeywordIndexWeb.html
#
# Author: Dang Doan
# Date: 2017.07.04

import sys
# Detect python version
python_major_version = sys.version_info[0]

# Input-output Parameters
raw_list = ' FrA01.8, FrA08.6, FrA10.6, FrA11.6, FrM07.1, FrM08.6, FrM27.1, FrM27.5, MoA03.12, MoA04.2, MoA19.4, MoM06.5, MoM12.6, MoM18.4, MoP01.14, MoP01.9, MoP02.12, MoP02.6, MoP02.8, MoP06.5, ThA12.2, ThA12.3, ThA27.2, ThM03.13, ThM10.1, ThM10.2, ThM11.2, ThM27.3, ThM27.5, ThP11.2, ThP11.4, ThP12.4, TuA02.6, TuM04.6, TuM04.9, TuM12.6, TuM24.3, TuP01.2, TuP01.3, TuP01.4, TuP05.5, TuP17.1, TuP17.5, WeM02.7, WeM09.6, WeM24.1, WeM27.4, WeM33.2, WeP12.5, WeP24.4'
paper_list = raw_list.split(",")
paper_list = [paper_code.strip() for paper_code in paper_list]

keyword = 'Dang 1st round selected'
output_file = keyword.replace(' ', '_')+'.csv'

source_list = [
  'IFAC17_ContentListWeb_1.html',
  'IFAC17_ContentListWeb_2.html',
  'IFAC17_ContentListWeb_3.html',
  'IFAC17_ContentListWeb_4.html',
  'IFAC17_ContentListWeb_5.html'
  ]

# Algorithm parameters
left_offset_time = 19
time_length = 11
right_offset = 4000
right_offset_title = 300
csv_splitter = '\t'  # tab


# # --- Begin use case 1 ---
# # This function can be used to obtain only titles, for rough scanning
# # Note that this part does not work with Python 3 due to non-Unicode encoding
# # of the source files. See the use case 2 for fixing this with Python 3
# def get_title(source_file, paper_code):
#     # Extract the title of the paper with paper_code from source_file
#     with open(source_file) as objFile:
#         text = objFile.read()
#
#     if (text.find(paper_code) >= 0):
#         position_code = text.find(paper_code)
#         selected_text = text[position_code:position_code+right_offset]
#         position_viewAbstract = selected_text.find('viewAbstract')
#         title_text = selected_text[position_viewAbstract:position_viewAbstract+right_offset_title]
#         position_start_title = title_text.find('>') + 1
#         position_end_title = title_text.find('<', position_start_title)
#         title = title_text[position_start_title:position_end_title]
#         return title
#
#
# # Get tiltes only
# result_lines = ['Keyword'+csv_splitter+'Paper_code'+csv_splitter+'Title'+'\n']
# for paper_code in paper_list:
#     for source_file in source_list:
#         title = get_title(source_file, paper_code)
#         if (title):
#             result_lines.append(keyword+csv_splitter+paper_code+csv_splitter+title+'\n')
#
# with open(output_file, "w") as objFile:
#     objFile.writelines(result_lines)
# # --- End use case 1 ---


# # --- Begin use case 2 ---
def get_time_title_abstract(source_file, paper_code):
    # Extract the title of the paper with paper_code from source_file
    if (python_major_version <= 2):
        with open(source_file) as objFile:
            text = objFile.read()

    if (python_major_version >= 3):
        with open(source_file, encoding="windows-1252") as objFile:
            text = objFile.read()

    position_code = text.find(paper_code)
    if (position_code >= 0):
        # Get time of day
        position_time = position_code-left_offset_time
        time_of_day = text[position_time:position_time+time_length]
        selected_text = text[position_code:position_code+right_offset]
        # Get title
        position_viewAbstract = selected_text.find('viewAbstract')
        title_text = selected_text[position_viewAbstract:position_viewAbstract+right_offset_title]
        position_start_title = title_text.find('>') + 1
        position_end_title = title_text.find('<', position_start_title)
        title = title_text[position_start_title:position_end_title]
        if (python_major_version <= 2):
            title = title.decode('windows-1252').encode('utf-8')
        # Get abstract
        position_Abstract = selected_text.find('Abstract:')
        abstract_text = selected_text[position_Abstract:-1]
        position_start_abstract = abstract_text.find('>') + 1
        position_end_abstract = abstract_text.find('</div>', position_start_abstract)
        abstract = abstract_text[position_start_abstract:position_end_abstract].strip()
        if (python_major_version <= 2):
            abstract = abstract.decode('windows-1252').encode('utf-8')
    else:  # a "NoneType" error if the explicit value will be raised in the "return" if variables not exists
        title = None
        time_of_day = None
        abstract = None

    return time_of_day, title, abstract  # return a tuple


# Get tiltes and more properties
result_lines = ['Keyword'+csv_splitter+'Date'+csv_splitter+'Time'+csv_splitter+'Code'+csv_splitter+'Title'+csv_splitter+'Abstract'+'\n']
for paper_code in paper_list:
    # Get date
    if (paper_code[0:2] == 'Mo'):
        date = '10.07.2017 Mon.'
    if (paper_code[0:2] == 'Tu'):
        date = '11.07.2017 Tue.'
    if (paper_code[0:2] == 'We'):
        date = '12.07.2017 Wed.'
    if (paper_code[0:2] == 'Th'):
        date = '13.07.2017 Thu.'
    if (paper_code[0:2] == 'Fr'):
        date = '14.07.2017 Fri.'
    for source_file in source_list:
        time_of_day, title, abstract = get_time_title_abstract(source_file, paper_code)
        if (title):
            result_lines.append(keyword+csv_splitter+date+csv_splitter+time_of_day+csv_splitter+paper_code+csv_splitter+title+csv_splitter+abstract+'\n')

if (python_major_version <= 2):
    with open(output_file, "w") as objFile:
        objFile.writelines(result_lines)

if (python_major_version >= 3):  # strings are already stored as Unicode
    with open(output_file, "w", encoding="utf-8") as objFile:
        objFile.writelines(result_lines)
# # --- End use case 2 ---

print('List of papers has been crawled into the file:\n'+'  '+output_file)
