import requests
import pprint
from http.cookiejar import MozillaCookieJar


## curl -d 'credential_0=cygate_arubalab&credential_1=Arubalabra2021' -c Activate-cookie.txt https://activate.arubanetworks.com/LOGIN
## curl -b Activate-cookie.txt https://activate.arubanetworks.com/api/ext/inventory.json?action=query


s = requests.session()
s.cookies = MozillaCookieJar('Activate-cookie.txt')

url = "https://activate.arubanetworks.com/LOGIN"

data = {
    'credential_0': 'Nooke',
    'credential_1': '34.mD82cE8q37@4Q9'
}

response = s.post(url=url, data=data)
s.cookies.save('Activate-cookie.txt', ignore_discard=True)
print (response, s.cookies)


url2 = "https://activate.arubanetworks.com/api/ext/folder.json?action=query"
s.cookies.load(filename='Activate-cookie.txt')
r = s.post(url=url2, cookies=s.cookies)
print (r.json)
