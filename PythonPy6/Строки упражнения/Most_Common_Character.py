def most_common_char(string):
    cstring=string.lower()
    sampleChar=None
    maxcount=0
    for y in cstring:
        each_character_count = cstring.count(y)
        if y==" ": continue
        elif each_character_count>=maxcount:
            maxcount=each_character_count
            sampleChar=y
    return (sampleChar)
