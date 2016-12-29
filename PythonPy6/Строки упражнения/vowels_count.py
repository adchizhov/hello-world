def total_vowels(string):
    count=0
    string=string.lower()
    vowels=['a', 'e', 'i', 'o', 'u']
    for char in string:
        if char in vowels:
            count=count+1
    return (count)
