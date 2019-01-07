#!/usr/bin/python2.7
import urllib2
import bs4 as bs
import time
from twilio.rest import Client

#Twilio API information for sms
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

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
        #output latest call
        print call_data[1].text
        #send text message
        sms_function()
        #if triggered, wait 1 hour
        time.sleep(3600)
    else:
        #output latest call
        print call_data[1].text
        #if not triggered, wait 30 secs
        time.sleep(30)

#sms information
def sms_function():
    client.messages.create(to="+[DEST PHONE NUM]",
                   from_="+[TWILIO PHONE NUM]",
                   body="A call matching your choosen filer has been triggered.")

#call function
while True:
    call_search()
