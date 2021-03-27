import pprint
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

for data in json_data['devices']:
     data_mac = data['mac']
     data_folder = data['additionalData']['folder']
     post_data = [('json','{ "devices" : [ { "mac" : "'+data_mac+'","folderName":"'+data_folder+'" } ] }')] ##kansioon mikä löytyy tiedostosta
     #post_data = [('json','{ "devices" : [ { "mac" : "'+data_mac+'","folderName":"VBO" } ] }')] ## määriteltyyn kansioon
     print(post_data)
     resp = s.post(url=url, cookies=cookies, data=post_data, params=params)
     print (resp.json())



##for data in indata:
  #data_mac = data['mac']
  #data_folder = data['additionalData']['folder']
  #print (data_mac, data_folder)
  #print('MacAddr:  ' + data['mac'])
  #r = s.post(url=url, cookies=cookies, data=data, params=params)
  #print (r.json())



#for p in indata:
#  r = s.post(url=url, cookies=cookies, data={'json':'{"devices":[{p['mac']}])
#  print('MacAddr:  ' + p['mac'])
#  print('Folder:  ' + p['additionalData']{'folder'})
#  print('Serial:  ' + p['serialNumber'])
#  #print ('')


#pprint.pprint(r.json())