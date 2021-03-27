import requests
from http.cookiejar import MozillaCookieJar

s = requests.session()
cookies = MozillaCookieJar(filename='Activate-cookie.txt')
cookies.load(filename='Activate-cookie.txt', ignore_discard=True, ignore_expires=False)

url = "https://activate.arubanetworks.com/api/ext/inventory.json?action=query"
resp = s.post(url=url, cookies=cookies)

count = 0
if resp and resp.status_code == 200:
    #print(resp.status_code)
    ap_inventory = resp.json()
    folder = input("folder to look for:")
else:
    print("ERROR:", resp.status_code, resp)

for data in ap_inventory['devices']:
    data_mac = data['mac']
    data_folder = data['additionalData']['folder']
    #print(data_mac, data_folder)
    if data['additionalData']['folder'] in folder:
        count +=1
        print("mac: ", data_mac, "folder:  ",data_folder)
print ("total aps", count)







