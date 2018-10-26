#!/usr/bin/env python
import sys
import os
import csv
import difflib
import re

def read_csv_table(csvFile):
    """
    Read a CSV file, export as a table: table[row][column]
    """
    table = []
    with open(filename, 'rt') as file_in:
        csv_reader = csv.reader(file_in, delimiter='\t')
        for r, row in enumerate(csv_reader):
            table.append(row)
    return table

def transpose_table(table):
    table_transpose = [[row[i] for row in table] for i in range(len(table[0]))]
    return table_transpose

def parse_table_column(table, numberColumn):
    #import time # testing with a table of 94044 rows, 4 columns
    columns = [[] for _ in range(numberColumn)]
    #start=time.time()
    for k in range(numberColumn):
        columns[k] = []
    for row in table:
        for k in range(numberColumn):
            columns[k].append(row[k])
    #end=time.time()
    #print(end-start) # 0.07465
    #start=time.time()
    #table_transpose = [[row[i] for row in table] for i in range(len(table[0]))]
    #end=time.time()
    #print(end-start) # 0.01496
    #start=time.time()
    #table_transpose2 = map(list, zip(*table))
    #end=time.time()
    #print(end-start) # 0.05046
    return columns
    
def compare_text_columns(table, column1Position, column2Position):
    similarity = list()
    for i in range(len(table)):
        sourceSentence = table[i][column1Position]
        targetSentence = table[i][column2Position]
        # Remove hyphen due to line break in German
        sourceSentence = re.sub(r'([A-Za-z])\- +(?!und |oder |bzw\. )([a-z])', r'\1\2', sourceSentence)
        table[i][column1Position] = sourceSentence
        targetSentence = re.sub(r'([A-Za-z])\- +(?!und |oder |bzw\. )([a-z])', r'\1\2', targetSentence)
        table[i][column2Position] = targetSentence
        similarity += [difflib.SequenceMatcher(None, sourceSentence, targetSentence).ratio()]
    return table, similarity


def insert_column_table(table, position, newColumn):
    # Insert newColumn as a list to table as a 2-dimension list, before column #position
    for i in range(len(table)):
        table[i].insert(position, newColumn[i])
    return table


def insert_blank_column_table(table, position):
    # Insert a blank column to table as a 2-dimension list, before column #position
    for i in range(len(table)):
        table[i].insert(position, '')
    return table


def write_table_csv(exportFile, table):
    with open(exportFile, 'wt') as csvfile:
        textWriter = csv.writer(csvfile, delimiter='\t')
        for i in range(len(table)):
            textWriter.writerow(table[i])

def sosanh_tu(file):  # for testing, table_de and table_en are global variables
    with open(file, 'rt') as text_file:
        text=text_file.read()
    start=time.time()
    matching = []
    for words in text:
        de_match=0
        en_match=0
        if words in table_de: de_match=1
        if words in table_en: en_match=2
        matching.append([de_match+en_match])
    end=time.time()
    time_cost=end-start
    return time_cost, matching

def two_set_match(text, set_1, set_2):
    matching = []
    for words in text:
        match_set_1=0
        match_set_2=0
        if words in set_1: match_set_1=1
        if words in set_2: match_set_2=2
        matching.append(match_set_1 + match_set_2)
    return matching

def multiple_set_match(text, *args):
    matching = []
    for words in text:
        match_item = 0
        for k in range(len(args)):
            if words in args[k]: match_item += 2**k
        matching.append(match_item)
    return matching

def test_mass_match(text_file, source_sets):
    # for testing, call: mass_compare(file, [table_de, table_en])
    import time
    with open(text_file, 'rt') as file_in:
        text=file_in.read()
    start=time.time()
    matching = multiple_set_match(text, *source_sets)
    end=time.time()
    time_cost=end-start
    return time_cost, matching

def mass_classification(text_file, csv_file, numberColumn):
    table = read_csv_table(csv_file)
    columns = parse_table_column(table, numberColumn)
    with open(text_file, 'rt') as file_in:
        text=file_in.read()
    matching = multiple_set_match(text, columns)
    return matching, text, columns
