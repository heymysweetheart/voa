#!/usr/bin/env python
#coding=utf-8

__author__ = 'leo'
import sys
import urllib2
import re
from bs4 import BeautifulSoup
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://www.51voa.com/Words_And_Idioms_{}.html'
base_url = 'http://www.51voa.com'

def parse_voa(url, base_rul, file):
    orderedDict = OrderedDict()
    soup = BeautifulSoup(urllib2.urlopen(url), "html.parser")
    #print soup.findAll('a')
    lists = soup.find(id='list').findAll('a')
    #for link in soup.find(id='list').findAll('a')
    #	print link.get('href')
    for article in lists:
    	article_link = article.get('href')
    	article_url = base_url + article_link
    	article_soup = BeautifulSoup(urllib2.urlopen(article_url), "html.parser")
    	article_title = article_soup.find(id='title').get_text()
    	if('：' in article_title):
    		article_title = article_title.replace('：', ' ')
    	article_title = re.sub('^\+?[1-9][0-9]*','',article_title)
    	article_content = article_soup.find(id='content').get_text()
    	result = re.sub("<.*?>", "", article_content)
    	if("(对不起,本课没有音频)" in result):
    		result = result.replace('(对不起,本课没有音频)', '')
    	orderedDict[article_title] = result

    items = orderedDict.items()
    items.reverse()
    newOrderedDict = OrderedDict(items)
    for key in newOrderedDict.keys():
    	print key
    	targetFile.write(('## '+key).encode('utf-8'))
    	targetFile.write('\n')
    	targetFile.write(newOrderedDict[key].encode('utf-8'))
    	targetFile.write('\n')
    	#print '## ' + key
    	#print newOrderedDict[key]
    	#print "-------------------------------------------------------"
    	#print article_title.get_text()
    	#print "-------------------------------------------------------"
    	#print article_content.get_text()

page = 17
targetFile = open('words_and_idioms.md', 'aw+')
while(page > 0):
    parse_voa(url.format(page), base_url, targetFile)
    page = page - 1
targetFile.close()
