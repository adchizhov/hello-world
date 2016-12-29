fhand = open('iamghost2.txt', 'r')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

print (sorted (counts))


fhand.close()
