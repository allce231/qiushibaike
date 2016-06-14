# -*- coding:utf-8 -*-

'''
糗事百科 -- python爬虫
web前端工程师：Hanson.Liu 360468937@qq.com
'''

import urllib
import urllib2
import MySQLdb
import re
import files
import time
import db

#糗事百科爬虫类
class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

        self.headers = {'User-Agent' : self.user_agent}

    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            #构建请求的request
            request = urllib2.Request(url,headers = self.headers)
            #利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            #将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接糗事百科失败,错误原因",e.reason
                return None

    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败...."
            return []
        pattern = re.compile('<div class="article .*?">.*?<div class="author .*?">.*?<h2>(.*?)</h2>.*?</div>.*?<div.*?'+
                         'content">(.*?)</div>(.*?)</div>',re.S)
        items = re.findall(pattern,pageCode)
        #用来存储每页的段子们
        pageStories = []
        #遍历正则表达式匹配的信息
        for item in items:
            #是否含有图片
            haveImg = re.search("img",item[2])
            #如果不含有图片，把它加入list中
            if not haveImg:
                pageStories.append({"title":item[0].strip(),"content":item[1].strip()})
        return pageStories

    def start(self,page):
        d = db.MySQL()
        for i in range(0,page):
            print '开始获取第'+ str(i+1) +'页数据'
            content = self.getPageItems(str(i))
            print '共获取到' +str(len(content))+ '数据';

            ##插入至数据库
            for item in content:
                d.insert('article',item)
            d.commit()
            print '插入到数据库成功'

            #延迟一秒加载下一页内容
            print '----------------------sleep3秒------------------------'
            time.sleep(3)


spider = QSBK()
spider.start(10)
