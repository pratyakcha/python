

def is_palindrome(teststr):
    #converting all the strings to lower cases
    temp = teststr.lower()
    #stripping punctuations and spaces
    newstr = ""
    for c in temp:
        if c.isalnum():
            newstr += c
    #calculating the reverse of the string
    reversestr = ""
    strindx = len(newstr) - 1
    while strindx >= 0:
        reversestr += newstr[strindx]
        strindx -=1
    if newstr == reversestr:
        return True
    return False


test_string = "Madam"
print(f"'{test_string}' is a palindrome: {is_palindrome(test_string)}")







