#Write a function that accepts
#a dictionary as input and returns a sorted list of all the keys in the dictionary.
def sort_key_dict(dict_input):
    x=list(dict_input.keys())
    x.sort()
    return (x)
#Write a function that accepts a dictionary as input and returns a 
#sorted list of all the values in the dictionary. Assume that the values 
#of this dictionary are just integers.
def sort_value_dict(dict_input):
    x=list(dict_input.values())
    x.sort()
    return (x)
