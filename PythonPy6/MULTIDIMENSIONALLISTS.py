my_course=[["Bunny",90,87,95],["Duck",78,96,89],["Rubble",83,85,92]]
for student_data in my_course:
    total_grade=0
    for grade_index in range(1,len(student_data)):
        total_grade=total_grade+student_data[grade_index]
    print ('The average for', student_data [0], 'is', total_grade/3.0)

lst=[[2,2,2],[3,3,3],[4,4,4]]

################### Sample Solution ###################
def _sum_of_a_2d_list_sample_(sample_2d_list):
    # Initialize total sum to be 0
    total_SUM = 0
    # Get the length of rows and columns
    number_of_rows = len(sample_2d_list)
    number_of_columns = len(sample_2d_list[0])
    # Initialize row index to 0
    rows = 0
    # Produce row indices 0, 1, 2, ...number_of_rows
    while rows < number_of_rows:
        # for each row, initialize the column index to 0
        columns = 0
        # Produce column indices 0, 1, 2, ... number_of_columns
        while columns < number_of_columns:
            # Added the element i.e. list[row][column] to total sum
            total_SUM = total_SUM + sample_2d_list[rows][columns]
            # Increment to the next column index
            columns = columns + 1
        # increment to the next row index
        rows = rows + 1
    # Finally return the total sum
    return total_SUM

################### Sample Solution ###################
def _average_of_a_2d_list_sample_(sample_2d_list):
    # Initialize total sum to be 0
    total_sum = 0
    number_of_items=0
    # Get the length of rows and columns
    for row_index in range(len(sample_2d_list)):
        for col_index in range(len(sample_2d_list[row_index])):
            total_sum=total_sum+sample_2d_list[row_index][col_index]
            number_of_items=number_of_items+1
    return total_sum/number_of_items

 
################### Sample Solution ###################
def _maximum_even_value_sample_(sample_2d_list):
    if not sample_2d_list: # list is empty
        return None
    result=None
    for row in sample_2d_list:
        row_max=_max_even_of_1d_list(row)
        if row_max:
            if result==None or row_max>result:
                result=row_max
    return result

def _max_even_of_1d_list(input_list):
    result=None
    for element in input_list:
        if element%2 ==0: # if element is even
            if result==None or element>result:
                result=element
    return result

 
################### Sample Solution ###################
def _sum_of_rows_sample_(sample_list):
    mylist = []
    for item in sample_list:
        mylist.append(sum(item))
    return mylist
    
