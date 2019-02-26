dictionary_char = {}
def dictionary(char, repeated, stringx) :
    dictionary_char[char] = repeated
    newstring = stringx.replace(char, "")
    return(char_freq(newstring))
def char_freq(stringname) :
    for i in stringname :
        count = 0
        for j in stringname :
            if j == i :
                count += 1
        return(dictionary(i, count, stringname))
string = "abbababababbbabadsbsbbab"
char_freq(string)
print(dictionary_char)
