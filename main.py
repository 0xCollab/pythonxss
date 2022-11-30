import requests

print("enter URL for scanning in https://yoururl.com format")
url = input()
if len(url)==0:
    print("no url to scan")
    exit(0)
else:
    r = requests.get(url)
    print(r.status_code)
    print(r.text)