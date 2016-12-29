def sorted_list(lst):
    copy=lst[:]
    copy.sort()
    if copy==lst:
        return True
    else:
        return False
