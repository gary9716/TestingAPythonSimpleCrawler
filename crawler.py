# coding=utf8
import urllib2
import csv
from codecs import open
from bs4 import BeautifulSoup
import pickle
import os
scriptPath = os.path.dirname(os.path.abspath(__file__))

#config
outputFileName = "parsedData.csv"
#parse the local file data_files/ClassSQList.html
urlToParse = "file:///" + scriptPath + "/data_files/ClassSQList.html" 
respData = urllib2.urlopen(urlToParse).read()
respData.decode('big5').encode('utf8')
soup = BeautifulSoup(respData)
allATag = soup.find_all("a", class_="step8_s")
#get rid of first url because it's an undesired one
allUrl = [ aTag['href'] for aTag in allATag[1:] ] 

numUrls = len(allUrl)


with open(outputFileName, 'wb', encoding='utf8') as csvfile:
  k = 1
  for singleUrl in allUrl:
      print 'processing url ' + str(k) + '/' + str(numUrls)
      urlToParse = singleUrl
      respData = urllib2.urlopen(urlToParse).read()
      respData.decode('big5').encode('utf8')
      soup = BeautifulSoup(respData)
      allTRTag = soup.find_all("tr")
      i = 0
      dataToCollect = []
      for singleTRTag in allTRTag:
        if i >= 15:
          break
        elif i >= 3:
          j = 0
          for child in singleTRTag.children:
            if j == 3 and child.string:
              dataToCollect.append(child.string.strip(u' ''   \t\n\r'))
            j+=1
        i+=1
      strToOutput = ','.join(['"' + string + '"' for string in dataToCollect]) + "\n"
      print strToOutput
      csvfile.write(strToOutput)
      k+=1
