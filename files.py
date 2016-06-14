# -*- coding:utf-8 -*-
import time
import sys
#文件类
class fileTxt:
    def __init__(self):
        #print 'txt'
        return
    def saveList(self,lists):
        reload(sys)                         # sys 主要用于解决保存txt 时出现的编码问题
        sys.setdefaultencoding('utf-8')     # 3
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        fo = open("pub/"+ t +".txt","w+")
        for item in lists:
            fo.write('anthor:'+item[0]+" content"+item[1]+"\r\n")
        fo.close()
        print '已保存'+t+'.txt'
