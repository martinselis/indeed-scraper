import requests
from bs4 import BeautifulSoup #importing HTML parser
import json

indeedUrl = 'https://www.indeed.co.uk/jobs?q='
linkList = [] #storing links here
textList = [] #output text is stored here. a list of dictionary objects {"company": company name, "job_title": job title, "text": raw text}
def start():
    limit = 0
    linkCount = 0
    loop = True
    job = input("Job title you want to be searched for: ")
    city =input("In which city? ")
    while loop:
        criteria = {'q': job, 'l': city, 'radius': 10, 'limit': 50, 'start': limit}
        global linkList
        global soup
        print ('link count', len(linkList))
        req = requests.get(indeedUrl, params=criteria)
        print (req.url)
        soup = BeautifulSoup(req.text, 'html.parser')

        resultDivs = soup.find_all("div", class_="jobsearch-SerpJobCard")
        for link in resultDivs:
            if len(link.find_all("span", class_="sponsoredGray")) > 0:
                continue
            fullUrl = "https://www.indeed.co.uk{}".format(link.a['href'])
            if fullUrl in linkList: 
                print('duplicate found') #if a duplicate link found, break. 
                loop = False
                break
            linkList.append(fullUrl)
        limit += 50 #move on to next page by adding +50 at the URL
    pullText()

#pulls text from individual links
def pullText():
    global textList
    i = 0
    for jobLink in linkList:
        linkReq = requests.get(jobLink)
        print ('getting jobinfo {} from {}'.format(i, linkReq.url))
        linkSoup = BeautifulSoup(linkReq.text, 'html.parser')
        i += 1
        findText(linkSoup) #once entire text retrieved, get the parts that are needed
    saveFile()

#gets the parts that are needed
def findText(linkSoup):
    addition= {}
    addition["job_title"] = linkSoup.find_all("h3", class_="jobsearch-JobInfoHeader-title")[0].string
    addition["company"] = linkSoup.find_all("div", class_="icl-u-xs-mr--xs")[0].string
    addition["text"] = linkSoup.find_all("div", class_="jobsearch-JobComponent-description")[0].text
    textList.append(addition)

def saveFile():
    with open ('data.json', 'w+') as fileSave:
        json.dump(textList, fileSave)

if __name__ == "__main__": 
    start()
