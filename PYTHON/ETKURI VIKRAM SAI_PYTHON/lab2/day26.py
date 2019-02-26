def newstring(stringname):
    stringx=stringname.translate({ord(i):None for i in"~!@#$%^&*():';<>?,./"})
    stringname=stringx.lower()
    return(stringname)
string=input()
stringx=newstring(string)
stringy=stringx[::-1]
if stringx==stringy:
    print("palindrome")
else:
    print("not palindrome")
