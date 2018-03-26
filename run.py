from ftntlib.ftntlib import FortiManagerJSON
import sys

devices = []
output = "NAME;IP;MASK"

hostname = sys.argv[1] 
username = sys.argv[2] 
password = sys.argv[3] 
adom = sys.argv[4] 

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
