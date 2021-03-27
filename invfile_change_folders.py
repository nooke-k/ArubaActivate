import requests
import json
from http.cookiejar import MozillaCookieJar

##curl -3 -d 'json={ "devices" : [ { "mac" : "6C:F3:7F:C3:54:42", "deviceName" : "steve-AP-105"} ] }' -b Activate-cookie.txt https://activate.arubanetworks.com/api/ext/inventory.json?action=update
#data = {
#  'json': '{ "devices" : [ { "mac" : "80:30:E0:8F:C8:80", "folderName":"default" } ] }'
#}

cookies = MozillaCookieJar(filename='Activate-cookie.txt')
cookies.load(filename='Activate-cookie.txt', ignore_discard=True, ignore_expires=False)
url = "https://activate.arubanetworks.com/api/ext/inventory.json"
params = "action=update"
s = requests.session()

with open('ap_inventory.json','r') as file:
  json_data = json.load(file)

##Look for items in certain folders and change the foldername:
for data in json_data['devices']:
    data_mac = data['mac']
    data_folder = data['additionalData']['folder']
    if data['additionalData']['folder'] in ["default"]: ##If folder is 'default'
        data['additionalData']['folder'] = "OSUUSKAUPPA_MAAKUNTA" ##change the folder to something else
        #print (data_mac, data_folder)
##dump the changed stuff to json file
with open('ap_inventory.json', 'w') as file:
  json.dump(json_data,file, indent=4)