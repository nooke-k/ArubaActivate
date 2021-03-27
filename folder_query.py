import pprint
import requests
from http.cookiejar import MozillaCookieJar
import json


## curl -b Activate-cookie.txt https://activate.arubanetworks.com/api/ext/folder.json?action=query


s = requests.session()
cookies = MozillaCookieJar(filename='Activate-cookie.txt')
cookies.load(filename='Activate-cookie.txt', ignore_discard=True, ignore_expires=False)

url = "https://activate.arubanetworks.com/api/ext/folder.json?action=query"

r = s.post(url=url, cookies=cookies)
respdata = r.json()
pprint.pprint(respdata['folders'])
##print('Foldername:   ' + i['folderName'] + '    FolderId:  '+ i['folderId'])
