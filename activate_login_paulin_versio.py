## curl -d 'credential_0=cygate_arubalab&credential_1=Arubalabra2021' -c Activate-cookie.txt https://activate.arubanetworks.com/LOGIN
## curl -b Activate-cookie.txt https://activate.arubanetworks.com/api/ext/inventory.json?action=query


import requests

url = "https://activate.arubanetworks.com/LOGIN"
data = {
    'credential_0': 'cygate_arubalab',
    'credential_1': 'Arubalabra2021'
}

s = requests.session()
r = s.post(url, data=data)
sessionId = {"csrf_token": s.cookies['csrf_token'], "session": s.cookies['session']}

print(sessionId)