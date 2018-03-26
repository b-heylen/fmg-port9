from ftntlib.ftntlib import FortiManagerJSON
import json
import ssl
import sys
import getopt
import getpass
import base64

devices = []
output = "NAME;IP;MASK"

hostname = server_IP 
username = user 
password = pwd 
adom = adom 

fmg = FortiManagerJSON()
response = fmg.login(hostname, username, password, ssl=True)

url = 'cli/global/system/global'
response = fmg._do('get',url)
wsMode  = response[1]["workspace-mode"]


url = '/dvmdb/adom/' + adom + '/device'
response = fmg.get(url, data="")

data = response[1]

for device in data:
  devices.append(device["name"])


for device in devices:
  url = 'pm/config/device/' + device + '/global/system/interface/port9'
  response = fmg.get(url, data="")

  addr = response[1]["ip"][0]
  mask = response[1]["ip"][1]

  output = output + "\n" + device + ";" + addr + ";" + mask

print("All port9 IP addresses:")
print(output)

fmg.logout()
