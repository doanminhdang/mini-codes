#!/usr/bin/env python
import sys
import os
import csv
# import unicodedata
import difflib

seriesFile = str(sys.argv[1])  # 1st argument is a list, specifying each file in one text line

# filePath = 'aligned_1__C15_Dien_tieng_Duc_lan_1_511-556-1__C15_Dien_tieng_Duc_lan_2_auflage_30_511-556.txt'

# with open(filename, 'rt', encoding='utf-8') as csvfile:
#     text = csv.reader(csvfile, dialect = 'excel-tab')
#     for row in text:
#         for smallStrings in row:
#             # Replade strange characters like \xad by popular characters
#             print(unicodedata.normalize("NFKD", smallStrings))
#         print(len(row))


def CompareTextCsv(filePath):
    table = list(csv.reader(open(filePath, 'rt'), delimiter='\t'))
    similarity = list()
    for i in range(len(table)):
        sourceSentence = table[i][0]
        targetSentence = table[i][1]
        similarity += [difflib.SequenceMatcher(None, sourceSentence, targetSentence).ratio()]
    print("Texts in columns 1 and 2 were compared.")
    return table, similarity


def WriteCompareTextCsv(exportFile, table, similarity):
    with open(exportFile, 'wt') as csvfile:
        textWriter = csv.writer(csvfile, delimiter='\t')
        for i in range(len(table)):
            textWriter.writerow(table[i][:2]+[similarity[i], '']+table[i][2:])


with open(seriesFile, 'r') as fileList:
    for line in fileList:
        filePath = line.rstrip('\n')
        table, similarity = CompareTextCsv(filePath)
        exportFile = os.path.join(os.path.dirname(filePath), 'compared_'+os.path.basename(filePath)+'.csv')
        WriteCompareTextCsv(exportFile, table, similarity)
        print("Data has been written to new file: "+exportFile)
