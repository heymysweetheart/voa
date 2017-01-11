__author__ = 'leo'

import urllib2
from bs4 import BeautifulSoup
from collections import OrderedDict

url = 'http://www.51voa.com/Learn_A_Word_{}.html'
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
    	#print base_url + article_link
    	article_url = base_url + article_link
    	article_soup = BeautifulSoup(urllib2.urlopen(article_url), "html.parser")
    	article_title = article_soup.find(id='title').get_text()
    	if(':' in article_title):
    		article_title = article_title.replace(':', ' ')
    	article_content = article_soup.find(id='content')
    	orderedDict[article_title] = article_content.get_text()
    #print orderedDict.items().reverse()
    #items = orderedDick.items().reverse()
    items = orderedDict.items()
    items.reverse()
    newOrderedDict = OrderedDict(items)
    for key in newOrderedDict.keys():
    	targetFile.write(('## ' + key).encode('utf-8'))
    	targetFile.write('\n')
    	targetFile.write(newOrderedDict[key].encode('utf-8'))
    	targetFile.write('\n')
    	#print '## ' + key
    	#print newOrderedDict[key]
    	#print "-------------------------------------------------------"
    	#print article_title.get_text()
    	#print "-------------------------------------------------------"
    	#print article_content.get_text()

page = 55
targetFile = open('target.md', 'aw+')
while(page > 0):
	parse_voa(url.format(page), base_url, targetFile)
	page = page -1
targetFile.close()
