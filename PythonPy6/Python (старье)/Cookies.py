current_number=23
current_divisor=2
current_number_is_prime=True
while (current_divisor<current_number):
    if current_number%current_divisor==0:
        current_number_is_prime=False
        break
    current_divisor=current_divisor+1
if current_number_is_prime:
    print (current_number, 'is prime')
print ('all done')


m = 0
my_str_1 = "university"
my_str_2 = "mississipy"
for char_1 in my_str_1:
    for char_2 in my_str_2:
        if char_1 == char_2:
            m = m + 1
print(m)
