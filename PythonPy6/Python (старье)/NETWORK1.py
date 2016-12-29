import urllib.request
handle=urllib.request.urlopen('http://py4inf.com/code/romeo.txt')
content =  handle.read().decode()
counts=dict()
for line in content:
    a=content.split()
    for word in a:
        counts[word]=counts.get(word,0)+1
print(counts)
