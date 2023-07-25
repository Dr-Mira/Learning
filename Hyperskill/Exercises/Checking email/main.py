def check_email(string):
    if (" " in string) or ('@' not in string) or ('@.' in string) or (string[0] == '@') or ('.' not in string) or (not
    string.find('@') < string.rfind('.')):
        return False
    else:
        return True
