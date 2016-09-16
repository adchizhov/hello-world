import random

seq = list(range (1, 7))
print(seq)

count = 0
y = 0
random.shuffle(seq)
print(seq)

for element in seq:
        for i in seq[seq.index(element): len(seq)]:
                if element > i:
                	count += 1

print (count)

