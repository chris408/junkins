import requests
import sys
import re

url = sys.argv[1]
#http_proxy = sys.argv[2]
#proxyDict = {"http" : http_proxy}
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

postdata = open('postdata', 'r')
#r = requests.post(url, headers=headers, proxies=proxyDict, data=postdata)
r = requests.post(url, headers=headers, data=postdata)
print r.text
postdata.close()
