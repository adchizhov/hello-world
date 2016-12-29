# This function will reverse string
def reverse_string(input_str):
    output_str="" #created an empty string
    for character in input_str:
        #print ("Character=", character)
        #print ("output_str=",output_str)
        output_str=character+output_str #this line will reverse
        #print ("output_str=",output_str)
    return (output_str)
# the second version
def reverse_string_v2 (input_str):
    output_str=""
    for k in range (len(input_str)-1,-1,-1):
        print (k)
        print (input_str[k])
string=reverse_string_v2("Hello")
print (string)
        
    
