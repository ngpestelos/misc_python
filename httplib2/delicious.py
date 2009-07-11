import httplib2

http = httplib2.Http()
response, content = http.request('http://feeds.delicious.com/v2/json/popular')
f = file('popular.json', 'w')
f.write(content)
f.close()
