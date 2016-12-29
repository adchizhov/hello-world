input_list=["we", "love", "python", "so","much"]
def slice_list (input_list):
    outputlist1=input_list[0:1]
    outputlist2=input_list[2:3]
    outputlist3=input_list[4:]
    xlist=[]
    xlist.extend(outputlist1)
    xlist.extend(outputlist2)
    xlist.extend(outputlist3)
    return (xlist)
