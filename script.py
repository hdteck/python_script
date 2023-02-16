#!/usr/bin/python3
 
import httplib2
 
http = httplib2.Http()
content = http.request("https://www.oil-price.net")[1]
 
print(content.decode())
