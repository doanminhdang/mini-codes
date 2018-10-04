#python3

import lxml.html

filename='petrol.html'
with open(filename,'r') as f:
  text=f.read()

html=lxml.html.fromstring(text)

newtext=lxml.html.tostring(html)
newfile='petrol2.html'
with open(newfile,'wb') as f:
  f.write(newtext)
#https://stackoverflow.com/questions/9487133/python-convert-html-ascii-encoded-text-to-utf8

import unescape
new2=unescape.unescape(text)

newfile2='petrol_unescape.html'
with open(newfile2,'wt') as f:
  f.write(new2)

#http://effbot.org/zone/re-sub.htm#unescape-html
