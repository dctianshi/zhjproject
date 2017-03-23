#encoding: utf-8
import xlwt

wbk=xlwt.Workbook()
sheet1=wbk.add_sheet("my_sheet1")

for i in range(1,10):
    for j in range(1,i+1):
        sheet1.write(i-1,j-1,"%sx%s=%s"%(j,i,j*i))

wbk.save(unicode(r"E:\python学习\learningcode\write.xls","utf-8"))