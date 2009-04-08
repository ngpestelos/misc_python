import httplib2

http = httplib2.Http()
local = http.request('http://127.0.0.1/')
print local
