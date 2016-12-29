input_string="Hello Python World"
def reverse_case_swap (input_string):
    swapcased=input_string.swapcase()
    output_str=""
    for character in swapcased:
        output_str=character+output_str #this line will reverse
    return (output_str)
