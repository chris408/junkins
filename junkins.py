import requests
import sys

url = sys.argv[1]
headers = {
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'close'
        }
f = open('plain_postdata', 'r')
postdata = f.read()
f.close()

try:
    r = requests.post(url, data={'script': postdata})
    print(r.text)
except:
    print("failed to connect to: %s" % url)
