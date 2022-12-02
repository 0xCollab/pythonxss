import requests
import sys
import urllib.parse
from bs4 import BeautifulSoup


# def validurl(str):
#    #r = requests.get(url)
#    if r.status_code == 200:
#        return url
#    else:
#        return exit(0)

# def fileopen(str):
#    f1 = open("payload.txt","r+")
#    for i in f1:
#        return i

def sendget(str):
    f1 = open('payload.txt').readlines()
    #    print (f1)
    for line in f1:
        #        payload = line
        #       print(payload)
        params = {'query': line}
        value = urllib.parse.urlencode(params)
        req = requests.get(str, params=params)
        #        print(req.url)
        #        print(req.headers)
        #        print(req.content)
        print(value)
        soup = BeautifulSoup(req.text)
        for value in doc.find_all(text=req.compile(), limit=2):
            print(value)
#        print(req.content)

print("enter URL for scanning in https://yoururl.com format")
url = input()
if len(url) == 0:
    print("no url to scan")
else:
    sendget(url)
