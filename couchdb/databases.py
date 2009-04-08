import httplib2

headers = {} 
headers.setdefault('Accept', 'application/json')
headers.setdefault('User-Agent', 'example couchdb client 0.1')

http = httplib2.Http()

resp, data = http.request('http://127.0.0.1:5984/_all_dbs', headers=headers)
print resp
print data
