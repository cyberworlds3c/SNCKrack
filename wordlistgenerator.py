import string

def wordlist(a, b, c) :

    char = ''

    if a == 1 :
        char+= string.digits

    if b == 1 :
        char+= string.ascii_lowercase

    if c == 1 :
        char+= string.ascii_uppercase

    else :
        char = string.ascii_letters + string.digits + '!#$%&*?@^~'

    return char