import requests

REST_BASE = 'http://localhost:8080/v1'
KVS_ENDPOINT = REST_BASE + '/kvs'

# Components of the Key
namespace = 'test'
setname = 'users'
userkey = 'bob'

record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
    base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)

response = requests.get(record_uri)
print("*** Got Record ***")
print(response.json())
