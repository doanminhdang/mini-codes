#!/usr/bin/env python
import sys
import os
import csv
# import unicodedata
import difflib

seriesFile = str(sys.argv[1])  # 1st argument is a list, specifying each file in one text line

# filePath = 'aligned_1__C15_Dien_tieng_Duc_lan_1_511-556-1__C15_Dien_tieng_Duc_lan_2_auflage_30_511-556.txt'

# with open(filePath, 'rt', encoding='utf-8') as csvfile:
#     text = csv.reader(csvfile, dialect = 'excel-tab')
#     for row in text:
#         for smallStrings in row:
#             # Replade strange characters like \xad by popular characters
#             print(unicodedata.normalize("NFKD", smallStrings))
#         print(len(row))


def CompareTextColumns(table, column1Position, column2Position):
    similarity = list()
    for i in range(len(table)):
        sourceSentence = table[i][column1Position]
        targetSentence = table[i][column2Position]
        similarity += [difflib.SequenceMatcher(None, sourceSentence, targetSentence).ratio()]
    return table, similarity


def InsertColumnTable(table, position, newColumn):
    # Insert newColumn as a list to table as a 2-dimension list, before column #position
    for i in range(len(table)):
        table[i].insert(position, newColumn[i])
    return table


def InsertBlankColumnTable(table, position):
    # Insert a blank column to table as a 2-dimension list, before column #position
    for i in range(len(table)):
        table[i].insert(position, '')
    return table


def WriteTableCsv(exportFile, table):
    with open(exportFile, 'wt') as csvfile:
        textWriter = csv.writer(csvfile, delimiter='\t')
        for i in range(len(table)):
            textWriter.writerow(table[i])


with open(seriesFile, 'r') as fileList:
    for line in fileList:
        filePath = line.rstrip('\n')
        table = list(csv.reader(open(filePath, 'rt'), delimiter='\t'))
        table, similarity = CompareTextColumns(table, 0, 1)
        table = InsertBlankColumnTable(table, 2)
        table = InsertColumnTable(table, 2, similarity)
        exportFile = os.path.join(os.path.dirname(filePath), 'compared_'+os.path.basename(filePath)+'.csv')
        WriteTableCsv(exportFile, table)
        print("Data has been written to new file: "+exportFile)
