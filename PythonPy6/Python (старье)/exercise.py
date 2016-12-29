#user=input ('Open file:')
handle=open('romeo.txt')
lst=list()
for line in handle:
    word=line.rstrip().split()
    print(word)
    for element in word:
        if element in lst:
            continue
        else:
            lst.append(element)
lst.sort()
print(lst)
    
    
def openFile():
    fname = raw_input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh

def startsWith():
    sw = raw_input("Enter line prefix to consider: ")
    if len(sw) < 1 : sw = "From"
    return sw

def printFrom(f,s):
    count = 0    
    for line in f:
        if line.startswith(s) and not line.startswith(s+':'):
            line = ((line.rstrip()).lstrip()).split()
            if (len(line) >= 2):
                print line[1]
                count=count+1
    return count


fh = openFile()
sw = startsWith()
result = printFrom(fh,sw)
print "There were",result,"lines in the file with From as the first word"
