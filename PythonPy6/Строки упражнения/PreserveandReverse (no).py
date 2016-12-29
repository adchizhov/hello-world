input_string= 'this is a sample test'
def preserve_reverse(input_string):
    splitted_list=input_string.split()
    for x in range (0, len(splitted_list)):
        splitted_list[x]=splitted_list[x][::-1]
    output_string = ""
    for x in range(0, len(splitted_list)):
        output_string += splitted_list[x] + " "
    # Strip any white spaces
    output_string = output_string.strip()
    return output_string
