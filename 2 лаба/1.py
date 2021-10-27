def palindrom(string):
    if str(string) == str(string)[::-1]:
        return True
    else:
        return False
