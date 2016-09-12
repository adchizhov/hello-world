import random

seq = list(range (1, 17))
print(seq)

is_sol = 1

random.shuffle(seq)
print(seq)

for index in range(len(seq)):
    if seq[index] > seq[index+1]:
        is_sol += 1

print (is_sol)
        
