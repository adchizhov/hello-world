import urllib.request
handle=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
content =  handle.read().decode()
print (content.strip())
