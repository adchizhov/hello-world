from urllib import *
fhand = urlopen ('http://rss.smorzhok.com/signin')
for line in fhand:
    print line.strip()
