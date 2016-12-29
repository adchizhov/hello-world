def palindrome(string):
    if str(string).lower()==str(string)[::-1].lower():
        return True
    else:
        return False
