engswe = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
x = "Y"
while x == "Y" :
    x = input("Enter a word? Y/N")
    if x == "N" :
        break
    y = input("Enter the word to translate : ")
    if y in engswe :
        print(engswe.get(y))
