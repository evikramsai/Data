listw = ["Hello","Hi","How","Are","You"]
def filter_long_words(listname, number) :
    for x in listname :
        if len(x) > number :
            print(x)

filter_long_words(listw, 3)
