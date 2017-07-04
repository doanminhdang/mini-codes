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

# Input-output Parameters
raw_list = ' FrA19.1, FrM27.1, FrM27.2, FrM27.3, FrM27.4, FrM27.5, MoA01.6, MoA01.11, MoA02.4, MoA02.6, MoA28.1, MoA28.2, MoM19.4, MoP22.2, MoP27.1, MoP27.3, MoP27.4, MoP27.5, MoP27.6, ThA14.3, ThA14.5, ThA22.2, ThA27.1, ThA27.5, ThM10.1, ThM10.2, ThM27.3, ThM27.5, ThM27.6, ThP13.5, ThP27.2, ThP27.4, ThP27.6, TuA14.2, TuA14.6, TuA22.6, TuA27.1, TuA27.2, TuA27.4, TuM27.1, TuM27.4, TuM27.5, WeM27.1, WeM27.2, WeM27.3, WeM27.4, WeM27.6, WeP19.2, WeP22.5, WeP27.1, WeP28.4'
paper_list = raw_list.split(",")

keyword = 'Model predictive and optimization-based control'
output_file = keyword+'.csv'

source_list = [\
'IFAC17_ContentListWeb_1.html',\
'IFAC17_ContentListWeb_2.html',\
'IFAC17_ContentListWeb_3.html',\
'IFAC17_ContentListWeb_4.html',\
'IFAC17_ContentListWeb_5.html'\
]

# Algorithm parameters
right_offset = 3000
right_offset_title =300
csv_splitter = ','

result_lines = []

def get_title(source_file, paper_code):
    # Extract the title of the paper with paper_code from source_file
    with open(source_file) as objFile:
        text = objFile.read()

    if (text.find(paper_code)>=0):
        position_code=text.find(paper_code)
        selected_text = text[position_code:position_code+right_offset]
        position_viewAbstract = selected_text.find('viewAbstract')
        title_text = selected_text[position_viewAbstract:position_viewAbstract+right_offset_title]
        position_start_title=title_text.find('>')+1
        position_end_title=title_text.find('<',position_start_title)
        title = title_text[position_start_title:position_end_title]
        return title

for paper_code in paper_list:
    for source_file in source_list:
        title = get_title(source_file, paper_code)
        if (title):
            result_lines.append(keyword+csv_splitter+paper_code+csv_splitter+title+'\n')

with open(output_file, "w") as objFile:
    objFile.writelines(result_lines)

print('List of papers has been crawled into the file:\n'+'  '+output_file)
