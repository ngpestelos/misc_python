import httplib2

http = httplib2.Http()
response, content = http.request('http://pipes.yahoo.com/pipes/pipe.run?_id=TmhtNVNu3hGMZlosjC6dVQ&_render=json')
f = file('hn.json', 'w')
f.write(content)
f.close()
