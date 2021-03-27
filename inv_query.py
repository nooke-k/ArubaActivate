from pprint import pprint
import requests
from http.cookiejar import MozillaCookieJar
import json

## curl -b Activate-cookie.txt https://activate.arubanetworks.com/api/ext/folder.json?action=query

s = requests.session()
cookies = MozillaCookieJar(filename='Activate-cookie.txt')
cookies.load(filename='Activate-cookie.txt', ignore_discard=True, ignore_expires=False)

url = "https://activate.arubanetworks.com/api/ext/inventory.json?action=query"

resp = s.post(url=url, cookies=cookies)

ap_inventory = resp.json()

#pprint (ap_inventory)

with open ('ap_inventory.json', 'w') as outfile:
 json.dump(ap_inventory,outfile, indent=4)


#pprint(dict.values(ap_inventory))
#pprint (ap_inventory['devices'])
#pprint(dict.items (ap_inventory))
####pprint(dict.items(ap_inventory['devices']))




