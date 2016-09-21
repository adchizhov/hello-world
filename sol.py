
random.shuffle(seq)
print(seq)

for element in seq:
        for i in seq[seq.index(element): len(seq)]:
                if element > i:
                	count += 1

print (count)

