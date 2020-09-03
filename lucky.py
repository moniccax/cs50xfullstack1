# Project: “I’m Feeling Lucky” Google Search
#Whenever I search a topic on Google, I don’t look at just one search result
#at a time. By middle-clicking a search result link (or clicking while hold-
#ing ctrl ), I open the first several links in a bunch of new tabs to read later.
#I search Google often enough that this workflow—opening my browser,
#searching for a topic, and middle-clicking several links one by one—is
#tedious. It would be nice if I could simply type a search term on the com-
#mand line and have my computer automatically open a browser with all
#the top search results in new tabs. Let’s write a script to do this.


import requests, sys, webbrowser, bs4
from urllib.parse import urlsplit
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
#a_website = "https://www.google.com"

# Open url in a new window of the default browser, if possible
#webbrowser.open_new_tab(a_website)
print("This is the name of the program:", str(sys.argv[1:]))
print('Googling...')
# display text while downloading the Google page

#Download the page using requests
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# TODO: Retrieve top search result links.
# requests
soup = BeautifulSoup(res.text, 'lxml')
#print(soup)
# Parse the HTML using BeautifulSoup TODO: Open a browser tab for each result.
#linkElems = soup.select('.r a')
i=0
arrayValidlinkElems = []
#Look through the HTML for a way to identify the tags with the page.find_all('a', href=True) function
linkElems = soup.find_all('a', href=True)


for linkElems in soup.find_all('a'):
    listValidlinkElems = linkElems.get('href')
    try:
        response = requests.get(listValidlinkElems)
        varstatus = response.status_code
    except Exception as e:
        varstatus = None
    if varstatus == 200:
        validlistValidlinkElems = listValidlinkElems
        print(validlistValidlinkElems)
        webbrowser.open(validlistValidlinkElems)
#    listValidlinkElems = linkElems.get('href')


#for i in arrayValidlinkElems
#print(arrayValidlinkElems[i])
#r1 = urlsplit(arrayValidlinkElems.get('href'))
#print(r1.geturl())
#r2 = urlsplit(r1.geturl())
#print(r2.geturl())

#r = requests.get(linkElems.get('href'))
    #, auth=('user', 'pass'))
    #r = requests.head(linkElems[i])
#varstatus = r.status_code
#    if  varstatus == 200:
#        arrayValidlinkElems[i]= linkElems[i].get('href')
#    i = i+1
#print(arrayValidlinkElems)
#print(linkElems)
print (len(listValidlinkElems))

numOpen = min(5, len(linkElems))
#for i in range(numOpen):
    #response = requests.get(listValidlinkElems[i])
    #varstatus = response.status_code
    #if  varstatus == 200:
    # print('o sistema é foda') ***********************
        #webbrowser.open(linkElems.get('href'))
        #webbrowser.open(linkElems.get('href'))
    #webbrowser.open( linkElems[i].attrs.get('href'), 2)
        #webbrowser.open(linkElems[i].attrs.get('href'))
