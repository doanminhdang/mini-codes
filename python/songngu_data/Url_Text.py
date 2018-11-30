#!/usr/bin/env python
# -*- coding: utf-8 -*-


## Using BeautifulSoup, need to install python-bs4
#from bs4 import BeautifulSoup
#import urllib2
#url="http://www.viet-studies.net/kinhte/ChinaBadOldDays_FA_trans.html"
#page=urllib2.urlopen(url)
#html_page=page.read()
#soup=BeautifulSoup(html_page)
#textonly = soup.get_text() # textonly has Unix-style end-of-line

## Using lxml and requests
#import requests
#import codecs
#from lxml import html
#url="http://www.viet-studies.net/kinhte/ChinaBadOldDays_FA_trans.html"
#page = requests.get(url)
#tree = html.fromstring(page.content)
#newtext=''.join(tree.xpath('//text()')) # newtext DOS-style end-of-line
#with codecs.open('url_text_lxml.txt',encoding='utf-8', mode='w+') as file:
  #file.write(newtext)

# Using lxml and urllib2. urllib2 is available in CentOS 6 of Hawkhost
import urllib2
import lxml.html
#import codecs
url="http://www.viet-studies.net/kinhte/ChinaBadOldDays_FA_trans.html"
page=urllib2.urlopen(url)
html_page=page.read()
newtree=lxml.html.fromstring(html_page)
text2=''.join(newtree.xpath('//text()'))

# Cleaning the text
# Note: the EOL character is \r\n
text2 = text2.replace('\r\n', '\n')
notab = text2.replace('\t', '')
replace_pattern = r'([^\n]) *\n(.)'
clean_text = re.sub(replace_pattern,r'\g<1> \g<2>', notab) 
#with codecs.open('clean_text.txt',encoding='utf-8', mode='w+') as new_text_file:
  #new_text_file.write(clean_text)
with open('clean_text.txt','wt') as new_text_file:
    new_text_file.write(clean_text.encode('utf-8'))
    
# Deal with PDF file in URL
import urllib
import os
pdf_url = 'http://www.viet-studies.net/kinhte/ChinaBadOldDays_FA.pdf'
pdf_file = pdf_url[pdf_url.rfind("/")+1:] # 'ChinaBadOldDays_FA.pdf'
urllib.urlretrieve(pdf_url, pdf_file)

# Download PDF with 
import urllib2

def download_file(download_url, file_save_path):
    response = urllib2.urlopen(download_url)
    with open(file_save_path, 'wb') as new_file:
        new_file.write(response.read())
    print("Completed")

download_file(pdf_url, pdf_file)

# Make clean text from PDF file
mainname, extname = os.path.splitext(pdf_file)
txt_file = mainname + '.txt'
convert_command = 'pdftotext ' + pdf_file + ' ' + txt_file
os.system(convert_command)

with open(txt_file, 'rt') as text_file:
    pdftext = text_file.read().decode('utf-8')

#replace_pattern_pdftext = r'([^\n]) *\n(.)'  # note that pdftotext save file with EOL character is \n
clean_pdftext = re.sub(replace_pattern_pdftext,r'\g<1> \g<2>', pdftext) 
with open(txt_file,'wt') as new_text_file:
    new_text_file.write(clean_pdftext.encode('utf-8'))
