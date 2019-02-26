string = input("Enter the String : ")
def check_pangram(stringname) :
    if len(set("abcdefghijklmnopqrstuvwxyz") - set(stringname.lower())) == 0 :
        print("It is Pangram!")
    else :
        print("It is not Pangram!")
check_pangram(string)
