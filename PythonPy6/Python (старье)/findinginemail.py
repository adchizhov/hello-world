line='Серебрякова Наталья Александровна <cna@osp35.ru>'
start=line.find('@')
end=line.find('>')
print (start)
print (end)
host=line[start+1:end]
print (host)

x = '40'
y = int(x) + 2
print (y)

print (len('banana')*7)

text = "X-DSPAM-Confidence:    0.8475";
start=text.find('0')
end=text.find('5')
print (start)
print (end)
print (text[23,29])
