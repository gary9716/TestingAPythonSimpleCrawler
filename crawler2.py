# coding=utf8
import urllib2
import csv
from codecs import open
from bs4 import BeautifulSoup
import os
scriptPath = os.path.dirname(os.path.abspath(__file__))

urlToParse = "file:///" + scriptPath + "/testCrawling/test2.html"
#urlToParse = "file://localhost/Users/lab430/Desktop/test/test2.html"
#urlToParse = "http://agrpmg.afa.gov.tw/agr-Sed/agrJsp/ClassSimpleQuery/ClassSQData.jsp?classID=203075"
respData = urllib2.urlopen(urlToParse).read()
respData.decode('big5').encode('utf8')

soup = BeautifulSoup(respData)
allTag = soup.find_all("tr")
i = 0
dataToCollect = []
for singleTag in allTag:
  if i >= 15:
    break
  elif i >= 3:
    j = 0
    for child in singleTag.children:
      if j == 1 and child.string:
        dataToCollect.append(child.string.strip(u' ''   \t\n\r'))
      j+=1
  i+=1

#print ','.join(['"' + string + '"' for string in dataToCollect])

with open('titleRow.csv', 'wb', encoding='utf8') as csvfile:
  csvfile.write(','.join(['"' + string + '"' for string in dataToCollect]) + "\n")
