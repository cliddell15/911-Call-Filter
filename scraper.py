#!/usr/bin/python2.7
#import libraries
import urllib2
import bs4 as bs
import time

#url
url = ""

#filter search
string = ""

def call_search ():
    #query website and return html to the variable soup
    source = urllib2.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'lxml')

    call_data = soup.find_all('tr')

    if string in call_data[1].text:
        print call_data[1].text
        print"success"
    else:
        print call_data[1].text
        print"failure"

    time.sleep(30)

#call function
while True:
    call_search()
