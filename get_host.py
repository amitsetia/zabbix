import json
from pprint import pprint
import requests

url = 'http://monitoring.vidooly.com/zabbix/api_jsonrpc.php'
headers = {"Content-Type":"application/json"}

data = json.dumps(
{
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "Zabbix"
    },
    "id": 1,
    "auth": None
}
)

res = requests.post(url,data,headers=headers)
res = res.json()
print 'user.login response'
pprint(res)
pprint(res['result'])

payload = json.dumps(
   { 
      "jsonrpc": "2.0",
      "method": "host.get",
      "params": {
        'output': ['hostid','name'],
        "selectParentTemplates": ["templateid","name"]
      },
      "auth": res['result'],
      "id":2,
   }
	)
res2 = requests.post(url,payload,headers=headers)
res2 = res2.json()
print "host.get response"
pprint(res2)