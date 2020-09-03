import requests, sys, webbrowser, bs4
from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup
import re
import requests, os, bs4
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True) #ensures that this folder exists
# starting url
# store comics in ./xkcdwhile not url.endswith('#'):
while not url.endswith('#'):
    print('Downloading page %s...' % url)
    # Download the page.
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
#Find the URL of the comic image.
    #idElem = soup.find_all(id=True)
# <div id = "comic">
#   <img src="">
#<div>

    comicElem = soup.find_all(id="comic")
    print (comicElem)
    for comicElem in soup.find_all(id="comic"):
        imgElem = comicElem.get("src")
    print(imgElem)
    #comicElem = soup.select('#comic img')
#get the correct <img> element from the BeautifulSoup object.
    if imgElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = imgElem[0].get('src')
        # Save the image to ./xkcd.
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')# TODO: Get the Prev button's url.
print('Done.')
