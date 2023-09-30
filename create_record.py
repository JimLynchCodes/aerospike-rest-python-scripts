import requests

REST_BASE = 'http://localhost:8080/v1'
KVS_ENDPOINT = REST_BASE + '/kvs'

# Components of the Key
namespace = 'test'
setname = 'users'
userkey = 'bob'

record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
    base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)

# The content to be stored into Aerospike.
bins = {
    'name': 'Bob',
    'id': 123,
    'color': 'Purple',
    'languages': ['Python', 'Java', 'C'],
}

# Stores the record
res = requests.post(record_uri, json=bins)

print("*** Saved Record ***")
print(res.json())
