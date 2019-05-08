def para2text(p):
  import re
  rs = p._element.xpath('.//w:t')
  special_element = {'textbox', 'tbl'}
  n_steps_back = 6
  pr=[None]*n_steps_back
  id_processed = []
  for el in rs:
      pr[0] = el
      for step_parent in range(1, n_steps_back): #trace back 5 steps
          pr[step_parent] = pr[step_parent-1].getparent()
          if pr[step_parent] != None:
              if re.search(r'\}(.+)$', pr[step_parent].tag).group(1) in special_element:
              # extract type of element: t, p, textbox, shape, tbl (=table)...
              # and compare with special tags
                id_this_parent = id(pr[step_parent])
                el.text = u'\n' + el.text + u'\n' # to split the text inside textboxes, tables with main text
                #if not id_this_parent in special_element: # don't do this, because we need a line break at the last element of the textbox
                    #el.text = u'\n' + el.text + u'\n' # to split the text inside textboxes, tables with main text
                    #id_processed.append(id_this_parent)
  return u''.join([r.text for r in rs])

#>>> pr1.tag
#'{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r'
#>>> pr2.tag
#'{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'
#>>> pr3.tag
#'{http://schemas.openxmlformats.org/wordprocessingml/2006/main}txbxContent'
#>>> pr4.tag
#'{urn:schemas-microsoft-com:vml}textbox'
#>>> pr5.tag
#'{urn:schemas-microsoft-com:vml}shape'


#>>> pr1.tag
#'{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r'
#>>> pr2.tag
#'{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'
#>>> pr3.tag
#'{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'
#>>> pr4.tag
#'{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'
#>>> pr5.tag
#'{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl'

# Comparison

import docx

doc2 = docx.Document('CDT_31.7.2017_vi-64.docx')
for para in doc2.paragraphs:
    print(para.text)
    # text in textbox and tables are omitted by para.text

print(para2text(doc2)
# text in textbox and tables are kept. However, if a paragraph is wrapped around a textbox/table, then in the DOCX/XML file, that paragraph can be splitted to before & after the textbox/table. Example:


#Trong chương trình hoặc khối chương trình thường có những lệnh chỉ thị truy cập vào một biến số nhất định. Điều này xảy ra qua biến số con trỏ, cũng còn được gọi là con trỏ. Thí dụ con trỏ được quy chiếu đến địa chỉ một biến số, thì trị số của
#
#(table)
#
#biến số này sẽ đọc và khối chương trình đó sẽ xử lý biến số mới này. Hình 2 cho ta thấy cách cấu tạo một biến số integer với tên là “đường kính”. Toán tử “địa chỉ” cho biết địa chỉ của một biến số.Hình 2: Cấu tạo một biến số

# Idea to improve: first use para.text to collect text without textboxes and tables, then scan for textboxes and tables and append their text to the end.
