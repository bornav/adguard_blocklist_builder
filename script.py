from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl
import requests
import json
import os
 
## CHANGE HERE ##
# ip address of AdGuard Home
# "http(s)://<adguardHomeIp:<port>"

# host = "http://10.0.0.5:80" 
# # user name
# userName = "admin"
# # password
# password = "JCc9r2Pb##"
 # "http(s)://<adguardHomeIp:<port>"
host = os.getenv('HOST')
userName = os.getenv('USER')
password = os.getenv('PASS')
file_path = os.getenv('LIST')
# block list 
# taken from Wally3K's Firebog https://firebog.net/
urls = []
try:
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line.startswith("http://") or line.startswith("https://"):
                urls.append(line)

    # Print the URLs or do further processing

except FileNotFoundError:
    print(f"File not found at path: {file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
# print(urls)
############ End Edits ################# 
# Open TLSv1 Adapter
class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1)
 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0', 'Content-type': 'application/json'}     
 
s = requests.Session()
s.mount(host, MyAdapter())
x = s.post(host + "/control/login", json.dumps({"name": userName, "password" : password}), headers=headers )
print(x.text)
 
for u in urls:
    filterObj = json.dumps({'url':u, "name":u,"whitelist":False})
    print(filterObj)
    x = s.post(host + "/control/filtering/add_url", data = filterObj, headers=headers)
    print(x.text)
 
 
 